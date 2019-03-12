def test_resource_get(test_resource):

    r = test_resource.get(1)

    assert r.status_code == 200
    assert r.json() == {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    }


def test_resource_post(test_resource):

    json = {"userId": 1, "id": 101, "title": "foo", "body": "bar"}

    r = test_resource.post(json=json)

    assert r.status_code == 201
    assert r.json() == json


def test_resource_put(test_resource):

    json = {"userId": 1, "id": 1, "title": "foo", "body": "bar"}

    r = test_resource.put(1, json=json)

    assert r.status_code == 200
    assert r.json() == json


def test_resource_delete(test_resource):

    r = test_resource.delete(1)
    print(r.content)
    assert r.status_code == 200
