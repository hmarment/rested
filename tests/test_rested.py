import os

from rested import setup
from rested.integration import Integration


def test_setup():

    clients = setup(
        os.path.join(os.path.dirname(__file__), "resources", "test_configuration.toml")
    )

    assert hasattr(clients, "test") and isinstance(clients.test, Integration)
