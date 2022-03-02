from django.urls import path

from api.views import (
        AssignmentList, 
        AssignmentSingleUpdateDelete,
        ChoiceList,
        ChoiceSingleCreateUpdateDelete,
        QuestionList,
        QuestionSingleCreateUpdateDelete,
)


app_name = 'api'


urlpatterns = [
        path('assignment/', AssignmentList.as_view(), name='assignment-list'),
        path('assignment/<int:pk>/', AssignmentSingleUpdateDelete.as_view(), name='assignment-crud'),
        path('choice/', ChoiceList.as_view(), name='choice-list'),
        path('choice/<int:pk>/', ChoiceSingleCreateUpdateDelete.as_view(), name='choice-crud'),
        path('question/', QuestionList.as_view(), name='question-list'),
        path('question/<int:pk>/', QuestionSingleCreateUpdateDelete.as_view(), name='question-crud')
        ]
