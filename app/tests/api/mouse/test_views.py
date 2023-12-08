import json

import pytest

from api.models import Mouse


@pytest.mark.django_db
def test_add_mouse(client):
    data = {"name": "test", "color": "test", "age": 1}
    response = client.post(
        "/api/v1/mouse", data=json.dumps(data), content_type="application/json"
    )
    assert response.status_code == 201
    assert response.data["name"] == data["name"]
    assert Mouse.objects.filter(name="test").exists()


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    mouses = Mouse.objects.all()
    assert len(mouses) == 0

    resp = client.post("/api/v1/mouse", {}, content_type="application/json")
    assert resp.status_code == 400

    mouses = Mouse.objects.all()
    assert len(mouses) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    mouses = Mouse.objects.all()
    assert len(mouses) == 0
    data = {"color": "test2", "age": 2}

    resp = client.post("/api/v1/mouse", data, content_type="application/json")
    assert resp.status_code == 400

    mouses = Mouse.objects.all()
    assert len(mouses) == 0


@pytest.mark.django_db
def test_get_single_movie(client):
    mouse = Mouse.objects.create(name="The Big Lebowski", color="test", age=1)
    resp = client.get(f"/api/v1/mouse_search/{mouse.id}")
    assert resp.status_code == 200
    assert resp.data["name"] == "The Big Lebowski"


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/v1/mouse_search/foo/")
    assert resp.status_code == 404
