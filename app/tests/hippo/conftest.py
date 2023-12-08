import pytest

from hippo.models import Hippo


@pytest.fixture(scope="function")
def add_hippo():
    def _add_hippo(name, color, age):
        hippo = Hippo.objects.create(name=name, color=color, age=age)
        return hippo

    return _add_hippo
