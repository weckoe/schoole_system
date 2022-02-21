import http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import (
    CreateUserSerializer,
    ReadUserSerializer,
    UpdateUserSerializer,
)
from authentication.models import User

from django.shortcuts import get_object_or_404

class UserListCreate(APIView, LimitOffsetPagination):
    queryset = User.objects.all()

    def get(self, request):
        results = self.paginate_queryset(self.queryset, request)
        serializer = ReadUserSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
   
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.validated_data)
 

class UserSingleUpdateDelete(APIView):
    queryset = User.objects.all()

    def get(self, request, pk):
        queryset = get_object_or_404(User, id=pk)
        serializer = ReadUserSerializer(queryset)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = UpdateUserSerializer(
                instance=user, 
                data=request.data
                )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.validated_data)

    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()
        return Response(status=http.HTTPStatus.ACCEPTED)
