# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

import requests

from .integration import Integration


class Rested:
    """
    A basic HTTP Rest client for API Integrations
    """
    def __init__(self, integrations=None):

        self._integrations = integrations if integrations else list()
        self._wire_integrations(integrations=self._integrations)

    @property
    def integrations(self):
        return self._integrations

    def _wire(self, integration=None):
        if integration and isinstance(integration, Integration):
            setattr(self, integration.name, integration)

            if integration not in self._integrations:
                self._integrations.append(integration)

    def integrate(self, integration=None):
        """
        Add a new API integration, accessible via
        Rested.<integration-name>.
        """
        self._wire(integration=integration)

    def _wire_integrations(self, integrations=None):
        """
        Wire integrations into Rested, each integration is accessible via
        Rested.<integration-name>.
        """
        for integration in integrations:
            self._wire(integration)


class Integrations:

    def __init__(self, inte)
