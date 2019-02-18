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

    # def _set_headers(self, headers=None):
    #     """Update default headers to include any additionals."""
    #     default_headers = ENDPOINTS.get('Headers', {})

    #     # calls to e.g. auth API might not be authenticated
    #     if self._is_authenticated():
    #         default_headers.update({'X-AUTH-TOKEN': self.token.token})
    #     if headers:
    #         default_headers.update(headers)
    #     return default_headers

    # def _build_url(self, *parts):
    #     """Enforce the slash."""
    #     parts = [self.base_url] + list(parts)
    #     return '/'.join(str(part).strip('/') for part in parts)
