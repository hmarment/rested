__version__ = "0.0.4"

from tomlkit import parse

from .integration import Integration
from .resource import Resource
from .method import Method
from .client import Rested
from .auth.auth import (
    BasicAuth,
    JwtAuth
)

AUTHENTICATION = {
    'Basic': BasicAuth,
    'JWT': JwtAuth
}

def _validate(config):
    return config

def _load_config(config_file_path):

    try:
        config_file_as_string = open(config_file_path, 'r').read()
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        config = _validate(parse(config_file_as_string))
        return config


def setup(*config_files):
    
    r = Rested()

    for config_file in config_files:
        
        config = _load_config(config_file)
        name = config['configuration']['name']
        base_url = config['configuration']['base-url']
        auth_type = config['configuration']['auth']
        resources = config['resources']

        auth = AUTHENTICATION.get(auth_type)

        integration = Integration(
            name=name,
            base_url=base_url,
            auth=auth,
        )

        for resource_name, methods in resources.items():

            resource = Resource(
                name=resource_name,
                integration=integration
            )

            for method_name, spec in methods.items():
                endpoint = spec.get('endpoint')
                http_method = spec.get('method')
                accepted_params = spec.get('arguments')
                method = Method(
                    name=method_name,
                    http_method=http_method,
                    resource=resource,
                    accepted_params=accepted_params,
                    )
                resource.register(method=method)

            integration.register(resource)
        r.integrate(integration)

    return r