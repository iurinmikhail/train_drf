import pytest

from api.models import Mouse
import logging


def create_mouse(**kwargs):
    Mouse.objects.create(**kwargs)


@pytest.mark.django_db
def test_mouse(mouses, delete_mouse):
    for mouse in mouses:
        create_mouse(**mouse)
    assert Mouse.objects.count() == 2


@pytest.mark.django_db
def test_list_mouses(mouses, delete_mouse):
    for mouse in mouses:
        create_mouse(**mouse)
    all_mouses = Mouse.objects.all()

    for add_mouse in all_mouses:
        assert add_mouse.to_dict() in mouses


@pytest.mark.django_db
@pytest.mark.usefixtures('delete_mouse')
class TestMouse:

    def test_mouse(self, mouses):
        for mouse in mouses:
            create_mouse(**mouse)
        assert Mouse.objects.count() == 2

    def test_list_mouses(self, mouses):
        for mouse in mouses:
            create_mouse(**mouse)
        all_mouses = Mouse.objects.all()

        for add_mouse in all_mouses:
            assert add_mouse.to_dict() in mouses
