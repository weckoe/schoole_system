from django.urls import path
from authentication.views import UserListCreate, UserSingleUpdateDelete


urlpatterns = [
        path('', UserListCreate.as_view()),
        path('<uuid:pk>/', UserSingleUpdateDelete.as_view()),
        ]
