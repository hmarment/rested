import pytest

from rested import Integration, Resource


@pytest.fixture(scope='session')
def setup_resource():
    """Set up a test resource."""
    print('Setting up a test resource for external integrations')
    return Resource(name='myresource')


@pytest.fixture(scope='session')
def setup_integration():
    """Set up a test resource."""
    print('Setting up a test integration for an API')
    return Integration(name='myapi')
