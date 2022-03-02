import http

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from api.models import Assignment, Choice, Question
from api.serializers import (
    ReadAssignmentSerializer,
    CreateAssignmentSerializer,
    UpdateAssignmentSerializer,
    ReadChoiceSerializer,
    CreateChoiceSerializer,
    UpdateChoiceSerializer,
    ReadQuestionSerializer,
    CreateQuestionSerializer,
    UpdateQuestionSerializer,
)


class AssignmentList(APIView, LimitOffsetPagination):
    queryset = Assignment.objects.all()

    def get(self, request):
        results = self.paginate_queryset(self.queryset, request)
        serializer = ReadAssignmentSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CreateAssignmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data['title'])


class AssignmentSingleUpdateDelete(APIView):

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

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data['teacher'].id)

    def delete(self, request, pk):
        assignment = get_object_or_404(Assignment, id=pk)
        assignment.delete()
        return Response(status=http.HTTPStatus.NO_CONTENT)


class ChoiceList(APIView, LimitOffsetPagination):
    queryset = Choice.objects.all()

    def get(self, request):
        results = self.paginate_queryset(self.queryset, request)
        serializer = ReadChoiceSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = CreateChoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data['title'])


class ChoiceSingleCreateUpdateDelete(APIView):
    def get(self, request, pk):
        choice = get_object_or_404(Choice, id=pk)
        serializer = ReadChoiceSerializer(choice)
        return Response(serializer.data)

    def patch(self, request, pk):
        choice = get_object_or_404(Choice, id=pk)
        serializer = UpdateChoiceSerializer(
            instance=choice,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data['title'])

    def delete(self, request, pk):
        assignment = get_object_or_404(Choice, id=pk)
        assignment.delete()
        return Response(status=http.HTTPStatus.NO_CONTENT)


class QuestionList(APIView, LimitOffsetPagination):
    queryset = Question.objects.all()

    def get(self, request):
        results = self.paginate_queryset(self.queryset, request)
        serializer = ReadQuestionSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = CreateQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data['question'])


class QuestionSingleCreateUpdateDelete(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, id=pk)
        serializer = ReadQuestionSerializer(question)
        return Response(serializer.data)

    def patch(self, request, pk):
        question = get_object_or_404(Question, id=pk)
        serializer = UpdateQuestionSerializer(
            instance=question,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data['question'])

    def delete(self, request, pk):
        question = get_object_or_404(Question, id=pk)
        question.delete()
        return Response(status=http.HTTPStatus.NO_CONTENT)
