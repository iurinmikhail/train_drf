import json

import pytest

from hippo.models import Hippo


@pytest.mark.django_db
def test_add_hippo(client):
    hippos = Hippo.objects.all()
    assert len(hippos) == 0

    response = client.post(
        "/hippo/",
        {
            "name": "Hippo",
            "color": "blue",
            "age": 10,
        },
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.data["name"] == "Hippo"

    hippos = Hippo.objects.all()
    assert len(hippos) == 1


@pytest.mark.django_db
def test_add_hippo_invalid_json(client):
    hippos = Hippo.objects.all()
    assert len(hippos) == 0

    response = client.post("/hippo/", {}, content_type="application/json")
    assert response.status_code == 400

    hippos = Hippo.objects.all()
    assert len(hippos) == 0


@pytest.mark.django_db
def test_add_hippo_invalid_json_keys(client):
    hippos = Hippo.objects.all()
    assert len(hippos) == 0

    response = client.post(
        "/hippo/",
        {
            "name": "Hippo",
            "color": "blue",
        },
        content_type="application/json",
    )
    assert response.status_code == 400

    hippos = Hippo.objects.all()
    assert len(hippos) == 0


@pytest.mark.django_db
def test_get_single_hippo(client):
    hippo = Hippo.objects.create(
        name="Kate",
        color="pink",
        age=10,
    )

    response = client.get(f"/hippo/{hippo.id}/")
    assert response.status_code == 200
    assert response.data["name"] == "Kate"


@pytest.mark.django_db
def test_get_single_hippo_v2(client, add_hippo):
    hippo = add_hippo(
        name="Kate",
        color="pink",
        age=10,
    )

    response = client.get(f"/hippo/{hippo.id}/")
    assert response.status_code == 200
    assert response.data["name"] == "Kate"


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/hippo/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_hippos(client, add_hippo):
    add_hippo(name="Hippo", color="blue", age=10)
    add_hippo("Kira", "purple", 10)
    response = client.get("/hippo/")
    assert response.status_code == 200
    assert response.data[0]["name"] == "Hippo"
    assert response.data[1]["name"] == "Kira"
