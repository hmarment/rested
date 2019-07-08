import logging
import requests

from .auth.auth import UserLogin
from .errors import HTTP_ERRORS

logFormatter = "%(asctime)s - %(levelname)s - %(module)s:%(funcName)s " "- %(message)s"
logging.basicConfig(format=logFormatter, level=logging.WARNING)
logger = logging.getLogger(__name__)


class HttpClient:
    def __init__(
        self,
        session=None,
        default_headers=None,
        logger=logger,
        auth=None,
        authenticated=False,
    ):

        self._session = session if session else requests.Session()
        self._default_headers = default_headers if default_headers else dict()
        self._logger = logger
        self._auth = auth
        self._authenticated = authenticated

    def _set_headers(self, headers=None):

        request_headers = self._default_headers

        if headers:
            request_headers.update(headers)

        return request_headers

    def _build_url(self, *parts):
        """Enforce the slash."""
        parts = list(parts)
        return "/".join(str(part).strip("/") for part in parts)

    def _set_login_method(self, credentials, method):
        """Set method for login call."""

        self._credentials = credentials
        self._login = UserLogin(self._credentials, method)

    def _authenticate(self):

        if not self._authenticated and self._auth:
            self._auth(self)

    def _request(self, http_method, url, headers=None, json=None, authenticate=True):
        """HTTP Request handler."""

        if authenticate and not self._authenticated:
            self._authenticate()

        headers = self._set_headers(headers=headers)

        self._logger.debug(
            "Request(method={}, url={}, headers={}, body={}".format(
                http_method, url, headers, json
            )
        )

        try:
            response = self._session.request(
                http_method, url, headers=headers, json=json
            )
            response.raise_for_status()
        except requests.HTTPError:
            raise HTTP_ERRORS[response.status_code]
        else:
            return response

    def _get(self, url, headers=None):
        """HTTP GET."""

        response = self._request("GET", url, headers=headers)

        return response

    def _post(self, url, headers=None, json=None):
        """HTTP POST."""

        response = self._request("POST", url, headers=headers, json=json)

        return response

    def _put(self, url, headers=None, json=None):
        """HTTP PUT."""

        response = self._request("PUT", url, headers=headers, json=json)

        return response

    def _delete(self, url, headers=None):
        """HTTP DELETE."""

        response = self._request("DELETE", url, headers=headers)

        return response
