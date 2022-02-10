import json
from django.core import serializers
from rest_framework import serializers
from rest_framework.response import Response
from .models import User


class CreateUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'password',
            'last_login',
            'is_superuser',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined',
            'id',
            'email',
            'image',
        ]
        extra_kwargs = {
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'is_active': {'write_only': True},
            'email': {'write_only': True},
        }


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'is_staff',
            'email',
            'last_login',
        ]
