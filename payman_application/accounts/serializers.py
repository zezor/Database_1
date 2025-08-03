from rest_framework.utils.representation import serializer_repr
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ("email","password")
