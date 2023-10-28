import pytest

from api.models import Mouse


@pytest.fixture
def delete_mouse():
    Mouse.objects.all().delete()


@pytest.fixture
def mouses():
    print("Подготовка данных")
    mouses = [
        {"name": "Misha", "color": "grey", "age": 37},
        {"name": "Sasha", "color": "black", "age": 10},
    ]
    return mouses
