__version__ = "0.1.0"

from tomlkit import parse

from .integration import Integration
from .resource import Resource
from .method import Method
from .client import Rested
from .auth.credentials import User
from .auth.auth import BasicAuth, JwtAuth

AUTHENTICATION = {"Basic": BasicAuth, "JWT": JwtAuth}


def _validate(config):
    return config


def _load_config(config_file_path):

    try:
        config_file_as_string = open(config_file_path, "r").read()
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        config = _validate(parse(config_file_as_string))
        return config


def _load_credentials(profile_name, auth_config):
    """Load credentials from config first. If not present, load from credentials file."""

    if "credentials" in auth_config:
        return User(**auth_config["credentials"])

    return User.from_cache(profile_name)


def setup(*config_files):

    r = Rested()

    for config_file in config_files:

        config = _load_config(config_file)
        name = config["configuration"]["name"]
        base_url = config["configuration"]["base-url"]
        auth_config = config["configuration"]["auth"]
        resources = config["resources"]

        auth_type = auth_config.get("type")
        login_resource_name = auth_config.get("login-resource")
        login_method_name = auth_config.get("login-method")
        credentials = _load_credentials(name, auth_config)
        auth = AUTHENTICATION.get(auth_type)()
        # client.amp._set_login_method(u, login)
        integration = Integration(
            name=name, base_url=base_url, auth=auth, credentials=credentials
        )

        for resource_name, methods in resources.items():

            resource = Resource(name=resource_name, integration=integration)

            for method_name, spec in methods.items():
                endpoint = spec.get("endpoint")
                http_method = spec.get("method")
                accepted_params = spec.get("arguments")
                authenticate = spec.get("authenticate", True)
                method = Method(
                    name=method_name,
                    http_method=http_method,
                    resource=resource,
                    accepted_params=accepted_params,
                    authenticate=authenticate,
                )
                resource.register(method=method)

                if (
                    resource_name == login_resource_name
                    and method_name == login_method_name
                ):
                    integration._set_login_method(
                        credentials=credentials, method=method
                    )

            integration.register(resource)
        r.integrate(integration)

    return r
