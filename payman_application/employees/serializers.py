from rest_framework.utils.representation import serializer_repr
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Employee


class EmployeesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'