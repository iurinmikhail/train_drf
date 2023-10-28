from django.urls import include, path, register_converter
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter

from .views import (CatApiView, DogApiView, ElefantApiView, MonkeyViewSet,
                    MouseApiSearchView, MouseApiView, MouseApiViewUpdate,
                    MouseDetailApiView, MouseListApiView, UserApiView, index)

router = SimpleRouter()
router.register("monkey", MonkeyViewSet, basename="monkey_api")


class LowercaseConverter:
    regex = r"[\w\-]+"
    dbs = {"base1": 1, "BASE2": 2}

    def to_python(self, value):
        for k in self.dbs.keys():
            if k.lower() == value.lower():
                return k
        code = 1
        details = "База данных определена неверно"
        diagnostics = f"Доступные базы данных: {', '.join(self.dbs.keys())}"
        data = {"code": code, "details": details, "diagnostics": diagnostics}
        return data

    def to_url(self, value):
        for k in self.dbs.keys():
            if k.lower() == value.lower():
                return k


register_converter(LowercaseConverter, "lowercase")

urlpatterns = [
    path("", index),
    path("v1/", UserApiView.as_view(), name="user_api"),
    path("v1/cat", CatApiView.as_view(), name="cat_api"),
    path("v1/dog", DogApiView.as_view(), name="dog_api"),
    path("v1/mouselist", MouseListApiView.as_view(), name="mouselist_api"),
    path("v1/elefant", ElefantApiView.as_view(), name="elefant_api"),
    path(
        "v1/elefant/<str:pk>/Patient/<int:pid>",
        ElefantApiView.as_view(),
        name="elefant_api",
    ),
    path("v1/mouse", MouseApiView.as_view(), name="mouse_api"),
    path("v1/mouse_search/<int:pk>", MouseApiSearchView.as_view(), name="mouse_search"),
    # path('v1/mouse/<int:pk>', MouseApiViewUpdate.as_view(), name='mouse_api'),
    path(
        "v1/mousedetail/<int:pk>", MouseDetailApiView.as_view(), name="mousedetail_api"
    ),
    path("v1/", include(router.urls)),
    # path('v1/monkey/<int:pk>', MonkeyViewSet.as_view({'put': "update"}), name='monkey_api'),
    # path('v1/monkey/', MonkeyViewSet.as_view({'get': "list", 'post': "create"}), name='monkey_api'),
    # path('v1/monkey/', MonkeyViewSet.as_view({'post': "create"}), name='monkey_api'),
]
