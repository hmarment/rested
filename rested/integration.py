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

    def __init__(self, name=None, base_url=None, resources=None, session=None):

        self.name = name
        self.base_url = base_url
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

    def _request(self, http_method, url, json=None):
        """HTTP Request handler."""

        logger.debug(
            "Request(method={}, url={}, body={}".format(http_method, url, json)
        )

        try:
            response = self._session.request(http_method, url, json=json)
            response.raise_for_status()
        except requests.HTTPError:
            raise HTTP_ERRORS[response.status_code]
        else:
            return response

    def _get(self, url):
        """HTTP GET."""

        response = self._request("GET", url)

        return response

    def _post(self, url, json=None):
        """HTTP POST."""

        response = self._request("POST", url, json=json)

        return response

    def _put(self, url, json=None):
        """HTTP PUT."""

        response = self._request("PUT", url, json=json)

        return response

    def _delete(self, url):
        """HTTP DELETE."""

        response = self._request("DELETE", url)

        return response
