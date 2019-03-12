# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division


from .new import New
from .integration import Integration


class Rested:
    """
    A basic HTTP Rest client for API Integrations
    """

    def __init__(self, integrations=None):

        self._integrations = integrations if integrations else list()
        self._wire_integrations(integrations=self._integrations)
        self.new = New(client=self)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self._integrations == other._integrations

    def __repr__(self):
        return 'Rested(integrations={})'.format(self.integrations)

    @property
    def integrations(self):
        return self._integrations

    def _add_integration(self, name=None, base_url=None, resources=None, session=None):
        integration = Integration(
            name=name, base_url=base_url, resources=resources, session=session)

        self._wire(integration=integration)

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
