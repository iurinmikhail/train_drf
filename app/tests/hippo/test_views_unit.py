import pytest
from django.http import Http404

from hippo.models import Hippo
from hippo.serializers import HippoSerializer
from hippo.views import HippoDetail, HippoList


def test_add_hippo(client, monkeypatch):
    payload = {"name": "Lebowski", "color": "comedy", "age": 19}

    def mock_create(self, payload):
        return "Lebowski"

    monkeypatch.setattr(HippoSerializer, "create", mock_create)
    monkeypatch.setattr(HippoSerializer, "data", payload)

    resp = client.post("/hippo/", payload, content_type="application/json")
    assert resp.status_code == 201
    assert resp.data["name"] == "Lebowski"


def test_add_movie_invalid_json(client):
    resp = client.post("/hippo/", {}, content_type="application/json")
    assert resp.status_code == 400


def test_add_movie_invalid_json_keys(client):
    resp = client.post(
        "/hippo/",
        {"name": "Lebowski", "color": "brown"},
        content_type="application/json",
    )
    assert resp.status_code == 400


def test_get_single_movie(client, monkeypatch):
    payload = {"name": "Lebowski", "color": "brown", "age": 8}

    def mock_get_object(self, pk):
        return 1

    monkeypatch.setattr(HippoDetail, "get_object", mock_get_object)
    monkeypatch.setattr(HippoSerializer, "data", payload)

    resp = client.get("/hippo/1/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Lebowski"


def test_get_single_hippo_incorrect_id(client):
    resp = client.get("/hippo/foo/")
    assert resp.status_code == 404


def test_get_all_hippo(client, monkeypatch):
    payload = [
        {"name": "Lebowski", "color": "red", "age": 99},
        {"name": "Old Men", "color": "green", "age": 20},
    ]

    def mock_get_all_movies():
        return payload

    monkeypatch.setattr(Hippo.objects, "all", mock_get_all_movies)
    monkeypatch.setattr(HippoSerializer, "data", payload)

    resp = client.get("/hippo/")
    assert resp.status_code == 200
    assert resp.data[0]["name"] == payload[0]["name"]
    assert resp.data[1]["name"] == payload[1]["name"]


def test_remove_hippo(client, monkeypatch):
    def mock_get_object(self, pk):
        class Hippo:
            @staticmethod
            def delete():
                pass

        return Hippo

    monkeypatch.setattr(HippoDetail, "get_object", mock_get_object)

    resp = client.delete("/hippo/1/")
    assert resp.status_code == 204


def test_remove_hippo_incorrect_id(client, monkeypatch):
    def mock_get_object(self, pk):
        raise Http404

    monkeypatch.setattr(HippoDetail, "get_object", mock_get_object)

    resp = client.delete("/hippo/99/")
    assert resp.status_code == 404


