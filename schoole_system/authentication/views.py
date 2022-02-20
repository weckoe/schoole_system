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
            return Response(status=http.HTTPStatus.ACCEPTED)
 

class UserSingleUpdateDelete(APIView):
    queryset = User.objects.all()

    def get(self, request, pk):
        queryset = User.objects.filter(id=pk)
        serializer = ReadUserSerializer(
            queryset, many=True
        )
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = UpdateUserSerializer(
                instance=User.objects.get(id=pk), 
                data=request.data
                )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=http.HTTPStatus.ACCEPTED)

    def delete(self, request, pk):
        User.objects.get(id=pk).delete()
        return Response(status=http.HTTPStatus.ACCEPTED)
