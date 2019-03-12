# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

import logging

logFormatter = "%(asctime)s - %(levelname)s - %(module)s:%(funcName)s " "- %(message)s"
logging.basicConfig(format=logFormatter, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Resource:
    """Rest API resource."""

    def __init__(self, name=None, client=None):

        self.name = name
        self._client = client

    def get(self, entity_id):
        """
        Fetch a specific entity for this resource.
        """

        url = self._client._build_url(self.name, entity_id)
        logger.debug("Request(url={}".format(url))
        return self._client._get(url)

    def post(self, json=None):
        """
        Create a new entity for this resource.
        """

        url = self._client._build_url(self.name)

        return self._client._post(url, json=json)

    def put(self, entity_id, json=None):
        """
        Update a specific entity for this resource.
        """

        url = self._client._build_url(self.name, entity_id)

        return self._client._put(url, json=json)

    def delete(self, entity_id):
        """
        Delete a specific entity for this resource.
        """

        url = self._client._build_url(self.name, entity_id)

        return self._client._delete(url)
