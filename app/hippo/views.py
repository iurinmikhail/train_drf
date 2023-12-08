from typing import Optional

from django.http import Http404
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hippo
from .serializers import HippoSerializer, CheckSerializer
from .tasks import multiply_hippo


class HippoCheck(APIView):
    def post(self, request, format=None):
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid():
            document_ids = serializer.validated_data['instance_rids']
            result = multiply_hippo.delay(document_ids)
            task_id = result.task_id
            result = result.get()
            return Response({"result": result, "task_id": task_id}, status=status.HTTP_200_OK)



class HippoList(APIView):
    def get(self, request, format=None):
        movies = Hippo.objects.all()
        serializer = HippoSerializer(movies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "color": openapi.Schema(type=openapi.TYPE_STRING),
                "age": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        )
    )
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

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "color": openapi.Schema(type=openapi.TYPE_STRING),
                "age": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        )
    )
    def put(self, request, pk, format=None):
        hippo = self.get_object(pk)
        serializer = HippoSerializer(hippo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        hippo = self.get_object(pk)
        serializer = HippoSerializer(hippo)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        hippo = self.get_object(pk)
        hippo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
