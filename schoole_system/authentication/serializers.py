import json
from django.core import serializers
from rest_framework import serializers
from rest_framework.response import Response
from .models import User


class CreateUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create_user(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        serializer = serializers.serialize('json', [new_user, ])
        return Response(json.loads(serializer))

    def update_user(self, pk, validated_data):
        updated_user, _ = User.objects.filter(id=pk).update_or_create(**validated_data)
        serializer = serializers.serialize('json', [updated_user, ])
        return Response(json.loads(serializer))


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

    def reading_all_users(self):
        serializer = serializers.serialize('json', User.objects.all())
        return Response(json.loads(serializer))
