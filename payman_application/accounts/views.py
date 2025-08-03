from logging import raiseExceptions

from _testcapi import raise_exception
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer


User = get_user_model()
# from .models import User
# Create your views here.
"""
View
-Handle user registration
-Expect an email and password - REQUIRED
-Validate email and password
-save the data
-Return a response to the client
"""

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Registration successful"})