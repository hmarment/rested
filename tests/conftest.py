import pytest

from rested import Integration, Resource


@pytest.fixture(scope='session')
def resource():
    """Set up a test resource."""
    print('Setting up a test resource for external integrations')
    return Resource(name='todos')


@pytest.fixture(scope='session')
def integration():
    """Set up a test resource."""
    print('Setting up a test integration for an API')
    return Integration(name='myapi',
                       base_url='https://jsonplaceholder.typicode.com')
