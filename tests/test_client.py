import pytest

from rested import Integration, Rested


@pytest.fixture(scope='module')
def setup_integrations():
    """Set up a test resource."""
    print('Setting up a test integrations for multiple APIs')
    return [Integration(name='myapi1'),
            Integration(name='myapi2'),
            Integration(name='myapi3')]


@pytest.fixture(scope='module')
def setup_client():
    """Set up a test client."""
    print('Setting up a test client for external integrations')
    return Rested(integrations=[])


@pytest.fixture(scope='module')
def setup_client_with_multiple_integrations(setup_integrations):
    """Set up a test client."""
    print('Setting up a test client with multiple integrations')
    return Rested(integrations=setup_integrations)


def test_client(setup_client):
    assert isinstance(setup_client, Rested)


def test_client_integrations(setup_client):
    assert hasattr(setup_client, 'integrations')
    assert isinstance(setup_client.integrations, list)


def test_client_add_integration(setup_client, setup_integration):
    setup_client.integrate(setup_integration)
    assert len(setup_client.integrations) == 1
    assert hasattr(setup_client, setup_integration.name)


def test_client_multiple_integrations(setup_client_with_multiple_integrations):
    assert len(setup_client_with_multiple_integrations.integrations) == 3
    assert hasattr(setup_client_with_multiple_integrations, 'myapi1') \
        and isinstance(
            setup_client_with_multiple_integrations.myapi1, Integration) \
        and hasattr(setup_client_with_multiple_integrations, 'myapi2') \
        and isinstance(
            setup_client_with_multiple_integrations.myapi2, Integration) \
        and hasattr(setup_client_with_multiple_integrations, 'myapi3') \
        and isinstance(
            setup_client_with_multiple_integrations.myapi3, Integration)
