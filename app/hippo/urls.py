from django.urls import path

from .views import HippoDetail, HippoList, HippoCheck

urlpatterns = [
    path("hippo/", HippoList.as_view()),
    path("hippo/<int:pk>/", HippoDetail.as_view()),
    path("hippo/v2/<int:pk>/", HippoDetail.as_view()),
    path("hippo/check", HippoCheck.as_view()),
]
