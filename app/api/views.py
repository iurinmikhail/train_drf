from django.forms import model_to_dict
from django.http import Http404, HttpResponse
from rest_framework import generics, serializers, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Cat, Dog, Elefant, Monkey, Mouse, User
from api.serializers import (DBValidationSerializer, DogSerializer,
                             ElefantSerializer, MonkeySerializer,
                             MouseSerializer, UserSerializer, dbs)


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CatApiView(APIView):
    def get(self, request):
        lst = Cat.objects.all().values()
        return Response({"data": lst})

    def post(self, request):
        cat_new = Cat.objects.create(
            name=request.data["name"],
            color=request.data["color"],
            age=request.data["age"],
        )
        return Response({"data": model_to_dict(cat_new)})


class DogApiView(APIView):
    def get(self, request):
        lst = Dog.objects.all().values()
        serializer = DogSerializer(lst, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dog_new = Dog.objects.create(
            name=request.data["name"],
            color=request.data["color"],
            age=request.data["age"],
        )

        return Response({"data": DogSerializer(dog_new).data})


class ElefantApiView(APIView):
    def get(self, request, pk: str, pid):
        serializer = DBValidationSerializer(data={"db": pk})
        serializer.is_valid()
        if not serializer.is_valid():
            code = 1
            message = "База данных определена неверно"
            diagnostics = f"Доступные базы данных: {', '.join(dbs.keys())}"
            data = {"code": code, "message": message, "diagnostics": diagnostics}
            return Response({"error": data}, status=400)

        db = serializer.data["db"]
        return Response({"db": db})

    def post(self, request):
        serializer = ElefantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk is None:
            return Response({"error": "pk is required"})

        try:
            elefant = Elefant.objects.get(id=pk)
        except Elefant.DoesNotExist as e:
            return Response({"error": str(e)})

        serializer = ElefantSerializer(instance=elefant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})


class MouseListApiView(generics.ListCreateAPIView):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer


class MouseApiViewUpdate(generics.UpdateAPIView):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer


class MouseDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer


class MouseApiView(APIView):
    def post(self, request):
        serializer = MouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk is None:
            return Response({"error": "pk is required"})

        try:
            elefant = Mouse.objects.get(id=pk)
        except Mouse.DoesNotExist as e:
            return Response({"error": str(e)})

        serializer = MouseSerializer(instance=elefant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})


class MouseApiSearchView(APIView):
    def get_object(self, pk):
        try:
            return Mouse.objects.get(id=pk)
        except Mouse.DoesNotExist as e:
            raise Http404

    def get(self, request, pk, format=None):
        mouse = self.get_object(pk=pk)
        serializer = MouseSerializer(mouse)
        return Response(serializer.data)


#  ViewSet


class MonkeyViewSet(viewsets.ModelViewSet):
    queryset = Monkey.objects.all()
    serializer_class = MonkeySerializer
