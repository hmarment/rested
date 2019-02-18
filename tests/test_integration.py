

def test_integration_resources(setup_integration):
    assert hasattr(setup_integration, 'resources')
    assert isinstance(setup_integration.resources, list)


def test_integration_add_resource(setup_integration, setup_resource):
    setup_integration.register(setup_resource)
    assert len(setup_integration.resources) == 1


def test_integration_build_url(setup_integration, setup_resource):

    url = setup_integration._build_url(setup_resource.name, 1)
    assert url == 'https://jsonplaceholder.typicode.com/todos/1'


def test_integration_build_url_str(setup_integration, setup_resource):

    url = setup_integration._build_url(setup_resource.name, '1')
    assert url == 'https://jsonplaceholder.typicode.com/todos/1'


def test_integration_build_url_with_slash(setup_integration, setup_resource):

    url = setup_integration._build_url(setup_resource.name + '/', '/1/')
    assert url == 'https://jsonplaceholder.typicode.com/todos/1'


def test_integration_get(setup_integration):

    r = setup_integration._get('https://jsonplaceholder.typicode.com/todos/1')

    assert r.status_code == 200
    assert r.json() == {
      "userId": 1,
      "id": 1,
      "title": "delectus aut autem",
      "completed": False
    }
