import http

from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView 
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from api.models import Assignment
from api.serializers import (
        ReadAssignmentSerializer, 
        CreateAssignmentSerializer,
        UpdateAssignmentSerializer,
)

from authentication.models import User


class AssignmentList(APIView, LimitOffsetPagination):
    queryset = Assignment.objects.all()

    def get(self, request):
        results = self.paginate_queryset(self.queryset, request)
        serializer = ReadAssignmentSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CreateAssignmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.validated_data)


class  AssignmentSingleUpdateDelete(APIView):
    
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, id=pk)
        serializer = ReadAssignmentSerializer(assignment)
        return Response(serializer.data)

    def patch(self, request, pk):
        assignment = get_object_or_404(Assignment, id=pk)
        serializer = UpdateAssignmentSerializer(
                instance=assignment,
                data=request.data
        )
        
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.validated_data['teacher'].id)

    def delete(self, request, pk):
        assignment = get_object_or_404(Assignment, id=pk)
        assignment.delete()
        return Response(status=http.HTTPStatus.ACCEPTED)
 
