from django.urls import path
from .views import index, UserApiView, CatApiView, DogApiView, ElefantApiView

urlpatterns = [
    path('', index),
    path('v1/', UserApiView.as_view(), name='user_api'),
    path('v1/cat', CatApiView.as_view(), name='cat_api'),
    path('v1/dog', DogApiView.as_view(), name='dog_api'),
    path('v1/elefant', ElefantApiView.as_view(), name='elefant_api'),
    path('v1/elefant/<int:pk>', ElefantApiView.as_view(), name='elefant_api'),
    ]