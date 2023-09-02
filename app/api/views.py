from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User, Cat, Dog, Elefant
from api.serializers import UserSerializer, DogSerialise, ElefantSerialise


def index(request):
    return HttpResponse('<h1>Hello World</h1>')


class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CatApiView(APIView):
    def get(self, request):
        lst = Cat.objects.all().values()
        return Response({'data': lst})

    def post(self, request):
        cat_new = Cat.objects.create(
            name=request.data['name'],
            color=request.data['color'],
            age=request.data['age'])
        return Response({'data': model_to_dict(cat_new)})

class DogApiView(APIView):
    def get(self, request):
        lst = Dog.objects.all().values()
        serializer = DogSerialise(lst, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = DogSerialise(data=request.data)
        serializer.is_valid(raise_exception=True)

        dog_new = Dog.objects.create(
            name=request.data['name'],
            color=request.data['color'],
            age=request.data['age'])

        return Response({'data': DogSerialise(dog_new).data})


class ElefantApiView(APIView):
    def post(self, request):
        serializer = ElefantSerialise(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response({'error': 'pk is required'})

        try:
            elefant = Elefant.objects.get(id=pk)
        except Elefant.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = ElefantSerialise(instance=elefant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data': serializer.data})