import pytest

from hippo.models import Hippo


@pytest.mark.django_db
def test_hippo_model():
    hippo = Hippo.objects.create(name="test", color="test", age=1)
    assert hippo.name == "test"
    assert hippo.color == "test"
    assert hippo.age == 1
    assert str(hippo) == hippo.name
