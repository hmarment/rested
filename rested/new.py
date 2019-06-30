# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division


class New:

    def __init__(self, client=None, integration=None):
        self._client = client
        self._integration = integration

    def integration(self, name=None, base_url=None, resources=None, session=None):
        """Add a new integration."""

        self._client._add_integration(name=name, base_url=base_url,
                                      resources=resources, session=session)

    def resource(self, name=None, integration=None):
        """Add a new resource."""

        if not integration:
            if self.integration:
                integration = self.integration

        self._integration._add_resource(name=name, integration=integration)
