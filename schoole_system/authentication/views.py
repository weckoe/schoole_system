from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CreateUpdateUserSerializer, ReadUserSerializer
from .models import User
import uuid

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        if request.method == 'GET':
            queryset = User.objects.all()
            serializer = ReadUserSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):
        if request.method == 'POST':
            queryset, _ = User.objects.get_or_create(**request.data)
            serializer = CreateUpdateUserSerializer(data=queryset, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(request.data)

    def patch(self, request):
        if request.method == 'PATCH':
            user_id = request.data['id']
            queryset, _ = User.objects.filter(id=user_id).update(**request.data)
            serializer = CreateUpdateUserSerializer(queryset)
            return Response(serializer.data)

    def delete(self, request):
        if request.method == 'DELETE':
            user_id = request.data['id']
            queryset, _ = User.objects.filter(id=user_id).delete()
            return Response(data=HTTPStatus.NOT_FOUND)
