
from .resource import Resource


class Integration:
    """Rest Integration for a specific API."""

    def __init__(self, name=None, resources=None):

        self.name = name
        self._resources = resources if resources else list()

    @property
    def resources(self):
        return self._resources

    def register(self, resource=None):
        """
        Add a new resource, accessible via
        Integration.<resource-name>.
        """
        if resource and isinstance(resource, Resource):
            setattr(self, resource.name, resource)

            if resource not in self._resources:
                self._resources.append(resource)
