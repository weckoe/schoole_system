from django.urls import path

from api.views import AssignmentList, AssignmentSingleUpdateDelete


urlpatterns = [
        path('', AssignmentList.as_view(), name='assignment-list'),
        path('<int:pk>/', AssignmentSingleUpdateDelete.as_view(), name='crud'),
        ]
