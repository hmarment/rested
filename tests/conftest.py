import pytest
import requests

import rested

from rested import Integration, Resource

GET_URL = "https://jsonplaceholder.typicode.com/posts/1"
GET_JSON = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
}

POST_URL = "https://jsonplaceholder.typicode.com/posts"
POST_JSON = {"userId": 1, "id": 101, "title": "foo", "body": "bar"}

PUT_URL = "https://jsonplaceholder.typicode.com/posts/1"
PUT_JSON = {"userId": 1, "id": 1, "title": "foo", "body": "bar"}

DELETE_URL = "https://jsonplaceholder.typicode.com/posts/1"


class MockResponse:
    def __init__(self, status_code, content=None):
        self.status_code = status_code
        self.content = content

    def json(self):
        if type(self.content) in [list, dict]:
            return self.content

    def raise_for_status(self):

        if self.status_code > 299:
            raise requests.HTTPError


def request_side_effect(http_method, url, json):

    if http_method == "GET" and url == GET_URL:
        return MockResponse(200, GET_JSON)

    if http_method == "GET" and url != GET_URL:
        return MockResponse(404, {})

    if http_method == "POST" and url == POST_URL and json == POST_JSON:
        return MockResponse(201, POST_JSON)

    if http_method == "PUT" and url == PUT_URL and json == PUT_JSON:
        return MockResponse(200, PUT_JSON)

    if http_method == "DELETE" and url == DELETE_URL:
        return MockResponse(200, "deleted")


@pytest.fixture
def test_integration(mocker):
    """Set up a test integration."""
    print("Setting up a test integration for an API")
    mocker.patch.object(
        rested.integration.requests.Session, "request", side_effect=request_side_effect
    )
    integration = Integration(
        name="myapi", base_url="https://jsonplaceholder.typicode.com"
    )
    return integration


@pytest.fixture
def test_resource(test_integration):
    """Set up a test resource."""
    print("Setting up a test resource for external integrations")
    return Resource(name="posts", client=test_integration)
