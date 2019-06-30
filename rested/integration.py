# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

import requests
import logging

from .new import New
from .resource import Resource
from .errors import HTTP_ERRORS

logFormatter = "%(asctime)s - %(levelname)s - %(module)s:%(funcName)s " "- %(message)s"
logging.basicConfig(format=logFormatter, level=logging.WARNING)
logger = logging.getLogger(__name__)


class Integration:
    """Rest Integration for a specific API."""

    def __init__(
        self,
        name=None,
        base_url=None,
        auth=None,
        default_headers=None,
        resources=None,
        session=None,
        authenticated=False,
    ):

        self.name = name
        self.base_url = base_url
        self._auth = auth
        self._default_headers = default_headers
        self._authenticated = authenticated
        self._resources = resources if resources else list()
        self._session = session if session else requests.Session()
        self.new = New(integration=self)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.name == other.name and self.base_url == other.base_url

    def __repr__(self):
        return 'Integration(name={}, base_url={}, resources={}, session={}' \
            .format(self.name, self.base_url, self._resources, self._session)

    @property
    def resources(self):
        return self._resources

    def _add_resource(self, name=None, client=None):

        resource = Resource(name=name, client=client)
        self.register(resource=resource)

    def register(self, resource=None):
        """
        Add a new resource, accessible via
        Integration.<resource-name>.
        """
        if resource and isinstance(resource, Resource):
            setattr(resource, "_client", self)
            setattr(self, resource.name, resource)

            if resource not in self._resources:
                self._resources.append(resource)

    def _build_url(self, *parts):
        """Enforce the slash."""
        parts = [self.base_url] + list(parts)
        return "/".join(str(part).strip("/") for part in parts)

    def _set_headers(self, headers=None):

        request_headers = dict()

        if headers:
            request_headers.update(headers)

        return request_headers

    def _authenticate(self):
        self._auth(self)
        # auth.login()

    def _refresh_authentication(self):
        if self.token and (self.token.expired() or self.token.about_to_expire()):
            self.token = self._authenticate()

    def _request(self, http_method, url, headers=None, json=None):
        """HTTP Request handler."""

        headers = self._set_headers(headers=headers)

        logger.debug(
            "Request(method={}, url={}, headers={}, body={}".format(http_method, url, headers, json)
        )
        
        try:
            response = self._session.request(http_method, url, headers=headers, json=json)
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
