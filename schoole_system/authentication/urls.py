from django.urls import path
from schoole_system.authentication.views import UserListCreate, UserSingleUpdateDelete


app_name = 'authentication'


urlpatterns = [
        path('', UserListCreate.as_view(), name='users-list'),
        path('<uuid:pk>/', UserSingleUpdateDelete.as_view(), name='crud'),
        ]
