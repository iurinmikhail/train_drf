from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hippo
from .serializers import HippoSerializer


class HippoList(APIView):
    def get(self, request, format=None):
        movies = Hippo.objects.all()
        serializer = HippoSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HippoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HippoDetail(APIView):
    def get_object(self, pk):
        try:
            return Hippo.objects.get(pk=pk)
        except Hippo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hippo = self.get_object(pk)
        serializer = HippoSerializer(hippo)
        return Response(serializer.data)
