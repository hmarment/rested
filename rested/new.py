# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

from .integration import Integration


class New:

    def __init__(self, client):
        self.client = client

    def integration(self, name=None, base_url=None, resources=None, session=None):
        """Add a new integration"""

        integration = Integration(
            name=name, base_url=base_url, resources=resources, session=session)

        self.client._wire(integration=integration)
