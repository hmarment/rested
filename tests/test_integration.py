

def test_integration_resources(integration):
    assert hasattr(integration, 'resources')
    assert isinstance(integration.resources, list)


def test_integration_add_resource(integration, resource):
    integration.register(resource)
    assert len(integration.resources) == 1


def test_integration_build_url(integration, resource):

    url = integration._build_url(resource.name, 1)
    assert url == 'https://jsonplaceholder.typicode.com/todos/1'


def test_integration_build_url_str(integration, resource):

    url = integration._build_url(resource.name, '1')
    assert url == 'https://jsonplaceholder.typicode.com/todos/1'


def test_integration_build_url_with_slash(integration, resource):

    url = integration._build_url(resource.name + '/', '/1/')
    assert url == 'https://jsonplaceholder.typicode.com/todos/1'


def test_integration_get(integration):

    r = integration._get('https://jsonplaceholder.typicode.com/todos/1')

    assert r.status_code == 200
    assert r.json() == {
      "userId": 1,
      "id": 1,
      "title": "delectus aut autem",
      "completed": False
    }


def test_integration_post(integration):

    json = {
        "userId": 1,
        "id": 101,
        "title": "foo",
        "body": "bar"
    }

    r = integration._post('https://jsonplaceholder.typicode.com/posts',
                          json=json)
    print(r.json())
    assert r.status_code == 201
    assert r.json() == json


def test_integration_put(integration):

    json = {
        "userId": 1,
        "id": 1,
        "title": "foo",
        "body": "bar"
    }

    r = integration._put('https://jsonplaceholder.typicode.com/posts/1',
                         json=json)

    assert r.status_code == 200
    assert r.json() == json


def test_integration_delete(integration):

    r = integration._delete(
        'https://jsonplaceholder.typicode.com/posts/1')
    print(r.content)
    assert r.status_code == 200
