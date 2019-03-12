import pytest

from rested import Integration, Rested


@pytest.fixture(scope="session")
def integrations():
    """Set up a test resource."""
    print("Setting up a test integrations for multiple APIs")
    return [
        Integration(name="myapi1"),
        Integration(name="myapi2"),
        Integration(name="myapi3"),
    ]


@pytest.fixture(scope="session")
def client():
    """Set up a test client."""
    print("Setting up a test client for external integrations")
    return Rested(integrations=[])


@pytest.fixture(scope="session")
def client_with_multiple_integrations(integrations):
    """Set up a test client."""
    print("Setting up a test client with multiple integrations")
    return Rested(integrations=integrations)


def test_client(client):
    assert isinstance(client, Rested)


def test__str__(client):
    assert client.__str__() == "{{'_integrations': {}, 'new': {}}}" \
        .format(client.integrations, client.new)


def test_client__eq__equal(client):
    assert client == Rested(integrations=[])


def test_client__eq__unequal(client, client_with_multiple_integrations):
    assert client != client_with_multiple_integrations


def test_client__repr__(client):
    assert client.__repr__() == 'Rested(integrations=[])'


def test_client_integrations(client):
    assert hasattr(client, "integrations")
    assert isinstance(client.integrations, list)


def test_client_add_integration(client, test_integration):
    client._add_integration(name=test_integration.name,
                            base_url=test_integration.base_url)
    assert len(client.integrations) == 1
    assert hasattr(client, test_integration.name)


def test_client_integrate(client, test_integration):
    client.integrate(test_integration)
    assert len(client.integrations) == 1
    assert hasattr(client, test_integration.name)


def test_client_multiple_integrations(client_with_multiple_integrations):
    assert len(client_with_multiple_integrations.integrations) == 3
    assert (
        hasattr(client_with_multiple_integrations, "myapi1")
        and isinstance(client_with_multiple_integrations.myapi1, Integration)
        and hasattr(client_with_multiple_integrations, "myapi2")
        and isinstance(client_with_multiple_integrations.myapi2, Integration)
        and hasattr(client_with_multiple_integrations, "myapi3")
        and isinstance(client_with_multiple_integrations.myapi3, Integration)
    )


def test_client_new(client, test_integration):

    client.new.integration(name="newapi",
                           base_url=test_integration.base_url)
    assert len(client.integrations) == 2
    assert hasattr(client, test_integration.name)


def test_client_new_existing(client, test_integration):

    client.new.integration(name=test_integration.name,
                           base_url=test_integration.base_url)
    assert len(client.integrations) == 2
    assert hasattr(client, test_integration.name)
