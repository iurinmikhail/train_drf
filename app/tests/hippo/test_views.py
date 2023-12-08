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


def test_get_single_hippo_incorrect_id(client):
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


@pytest.mark.django_db
def test_remove_hippo(client, add_hippo):
    hippo = add_hippo(name="Lebowski", color="grey", age=8)

    resp = client.get(f"/hippo/{hippo.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Lebowski"

    resp_two = client.delete(f"/hippo/{hippo.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get("/hippo/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_hippo_incorrect_id(client):
    resp = client.delete(f"/hippo/99/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_hippo(client, add_hippo):
    hippo = add_hippo(name="The Big Lebowski", color="comedy", age=18)

    resp = client.put(
        f"/hippo/{hippo.id}/",
        {"name": "The Big Lebowski", "color": "comedy", "age": 19},
        content_type="application/json",
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "The Big Lebowski"
    assert resp.data["age"] == 19

    resp_two = client.get(f"/hippo/{hippo.id}/")
    assert resp_two.status_code == 200
    assert resp_two.data["name"] == "The Big Lebowski"
    assert resp.data["age"] == 19


@pytest.mark.django_db
def test_update_hippo_incorrect_id(client):
    resp = client.put(f"/hippo/99/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_hippo_invalid_json(client, add_hippo):
    hippo = add_hippo(name="The Big Lebowski", color="comedy", age="1998")
    resp = client.put(f"/hippo/{hippo.id}/", {}, content_type="application/json")
    assert resp.status_code == 400


@pytest.mark.django_db
def test_update_hippo_invalid_json_keys(client, add_hippo):
    hippo = add_hippo(name="The Big Lebowski", color="comedy", age="1998")

    resp = client.put(
        f"/hippo/{hippo.id}/",
        {"name": "The Big Lebowski", "color": "comedy"},
        content_type="application/json",
    )
    assert resp.status_code == 400


@pytest.mark.django_db
@pytest.mark.parametrize(
    "add_hippo, payload, status_code",
    [
        ("add_hippo", {}, 400),
        ("add_hippo", {"name": "The Big Lebowski", "color": "gold"}, 400),
    ],
    indirect=["add_hippo"],
)
def test_update_hippo_invalid_json(client, add_hippo, payload, status_code):
    hippo = add_hippo(name="The Big Lebowski", color="silver", age=19)
    resp = client.put(
        f"/hippo/{hippo.id}/",
        payload,
        content_type="application/json",
    )
    assert resp.status_code == status_code
