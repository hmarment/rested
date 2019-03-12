import requests


class MockResponse:
    def __init__(self, status_code, content=None):
        self.status_code = status_code
        self.content = content

    def json(self):
        if type(self.content) in [list, dict]:
            return self.content


def test_integration_resources(test_integration):
    assert hasattr(test_integration, "resources")
    assert isinstance(test_integration.resources, list)


def test_integration_add_resource(test_integration, test_resource):
    test_integration.register(test_resource)
    assert len(test_integration.resources) == 1


def test_integration_build_url(test_integration, test_resource):

    url = test_integration._build_url(test_resource.name, 1)
    assert url == "https://jsonplaceholder.typicode.com/posts/1"


def test_integration_build_url_str(test_integration, test_resource):

    url = test_integration._build_url(test_resource.name, "1")
    assert url == "https://jsonplaceholder.typicode.com/posts/1"


def test_integration_build_url_with_slash(test_integration, test_resource):

    url = test_integration._build_url(test_resource.name + "/", "/1/")
    assert url == "https://jsonplaceholder.typicode.com/posts/1"


def test_integration_get(test_integration):

    r = test_integration._get("https://jsonplaceholder.typicode.com/posts/1")

    assert r.status_code == 200
    assert r.json() == {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    }


def test_integration_post(test_integration):

    json = {"userId": 1, "id": 101, "title": "foo", "body": "bar"}

    r = test_integration._post("https://jsonplaceholder.typicode.com/posts", json=json)
    print(r.json())
    assert r.status_code == 201
    assert r.json() == json


def test_integration_put(test_integration):

    json = {"userId": 1, "id": 1, "title": "foo", "body": "bar"}

    r = test_integration._put("https://jsonplaceholder.typicode.com/posts/1", json=json)

    assert r.status_code == 200
    assert r.json() == json


def test_integration_delete(test_integration):

    r = test_integration._delete("https://jsonplaceholder.typicode.com/posts/1")
    print(r.content)
    assert r.status_code == 200
