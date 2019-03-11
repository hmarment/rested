def test_resource_get(resource):

    r = resource.get(1)

    assert r.status_code == 200
    assert r.json() == {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False,
    }


def test_resource_post(resource):

    json = {"userId": 1, "id": 201, "title": "foo", "body": "bar"}

    r = resource.post(json=json)

    assert r.status_code == 201
    assert r.json() == json


def test_resource_put(resource):

    json = {"userId": 1, "id": 1, "title": "foo", "body": "bar"}

    r = resource.put(1, json=json)

    assert r.status_code == 200
    assert r.json() == json


def test_resource_delete(resource):

    r = resource.delete(1)
    print(r.content)
    assert r.status_code == 200
