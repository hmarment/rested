# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

from .http import HttpClient
from .method import Method


class Resource:
    """Rest API resource."""

    def __init__(
        self, name=None, integration=None, methods=None, auth=None, login=None
    ):

        # super(Resource, self).__init__(
        #     session=integration._session,
        #     default_headers=integration._default_headers,
        #     auth=auth
        # )
        self.name = name
        self._integration = integration
        self._methods = methods if methods else list()
        self._login = login

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Resource(name={}, client={}".format(self.name, self._integration)

    def _build_url(self, *parts):
        return self._integration._build_url(self.name, *parts)

    def _add_method(self, name=None):

        method = Method(name=name, resource=self)
        self.register(method=method)

    def register(self, method=None):
        """
        Add a new method, accessible via
        Resource.<method-name>.
        """
        if method and isinstance(method, Method):
            setattr(method, "_resource", self)
            setattr(self, method.name, method)

            if method not in self._methods:
                self._methods.append(method)

    def get(self, entity_id, *url_params):
        """
        Fetch a specific entity for this resource.
        """

        url = self._build_url(entity_id, *url_params)
        self._integration._logger.debug("Request(url={}".format(url))
        return self._integration._get(url)

    def post(self, json=None, *url_params):
        """
        Create a new entity for this resource.
        """

        url = self._build_url(*url_params)

        return self._integration._post(url, json=json)

    def put(self, entity_id, json=None, *url_params):
        """
        Update a specific entity for this resource.
        """

        url = self._build_url(entity_id, *url_params)

        return self._integration._put(url, json=json)

    def delete(self, entity_id, *url_params):
        """
        Delete a specific entity for this resource.
        """

        url = self._build_url(entity_id, *url_params)

        return self._integration._delete(url)
