

def test_client_resources(setup_integration):
    assert hasattr(setup_integration, 'resources')
    assert isinstance(setup_integration.resources, list)


def test_client_add_resource(setup_integration, setup_resource):
    setup_integration.register(setup_resource)
    assert len(setup_integration.resources) == 1
