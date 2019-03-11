# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

import requests

from .resource import Resource


class Integration:
    """Rest Integration for a specific API."""

    def __init__(self, name=None, base_url=None, resources=None, session=None):

        self.name = name
        self.base_url = base_url
        self._resources = resources if resources else list()
        self._session = session if session else requests.Session()

    @property
    def resources(self):
        return self._resources

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

        with self._session as session:
            with session.request(http_method, url, json=json) as response:
                return response

    def _get(self, url):

        response = self._request("GET", url)

        return response

    def _post(self, url, json=None):

        response = self._request("POST", url, json=json)

        return response

    def _put(self, url, json=None):

        response = self._request("PUT", url, json=json)

        return response

    def _delete(self, url):

        response = self._request("DELETE", url)

        return response
