# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

from .http import HttpClient
from .method import Method

class Resource(HttpClient):
    """Rest API resource."""

    def __init__(self, name=None, integration=None, methods=None):

        super(Resource, self).__init__(
            session=integration._session,
            default_headers=integration._default_headers
        )
        self.name = name
        self._integration = integration
        self._methods = methods if methods else list()

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return 'Resource(name={}, client={}' \
            .format(self.name, self._integration)

    def _build_url(self, *parts):
        return super()._build_url(self._integration.base_url, *parts)

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

    def get(self, entity_id):
        """
        Fetch a specific entity for this resource.
        """

        url = self._build_url(self.name, entity_id)
        self._logger.debug("Request(url={}".format(url))
        return self._get(url)

    def post(self, json=None):
        """
        Create a new entity for this resource.
        """

        url = self._build_url(self.name)

        return self._post(url, json=json)

    def put(self, entity_id, json=None):
        """
        Update a specific entity for this resource.
        """

        url = self._build_url(self.name, entity_id)

        return self._put(url, json=json)

    def delete(self, entity_id):
        """
        Delete a specific entity for this resource.
        """

        url = self._build_url(self.name, entity_id)

        return self._delete(url)
