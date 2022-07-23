from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .import serializers
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    @swagger_auto_schema(operation_summary="Create User")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)