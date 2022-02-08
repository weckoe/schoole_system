from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CreateUpdateUserSerializer, ReadUserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    def users_list(self, request):
        queryset = User.objects.all()
        serializer = ReadUserSerializer(queryset, many=True)
        return Response(serializer.data)
