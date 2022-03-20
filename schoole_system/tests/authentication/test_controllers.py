from uuid import UUID

from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from authentication.models import User


class TestUserListView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            id=UUID('4b6ce8b2-789d-46fc-822f-7bbb4ee3956f'),
            first_name='Kirill',
            last_name='Lishtvan',
            email='kirilllisthvantest@gmail.com',
            is_student=True,
        )
        self.user.set_password('kirilltest123432')
        self.user.save()

    def test_get_all_users_view(self):
        url = reverse('authentication:users-list')
        response = self.client.get(url)
        self.assertEqual(response.data['results'][0]['email'], self.user.email)

    def test_get_single_student_view(self):
        url = reverse(
            'authentication:crud',
            kwargs={'pk': str(self.user.id)}
        )
        response = self.client.get(url)
        self.assertEqual(response.data['email'], self.user.email)

    def test_create_user_view(self):
        url = reverse(
            'authentication:users-list',
        )
        response = self.client.post(
            url,
            data={
                'email': 'emailfortests@gmail.com',
                'password': '123321test',
                'password2': '123321test',
                'first_name': 'Aleksey',
                'last_name': 'Sidorov',
                'is_student': 'false',
            },
            content_type="application/json",
        )
        self.assertEqual(response.data['email'], 'emailfortests@gmail.com')
        self.assertEqual(
            User.objects.get(email=response.data['email']).last_name,
            'Sidorov'
        )

    def test_update_user_view(self):
        url = reverse(
            'authentication:crud',
            kwargs={'pk': str(self.user.id)}
        )
        response = self.client.patch(
            url,
            data={
                'last_name': 'Arturov',
                'first_name': 'Maks',
                'email': 'test123@gmail.com',
                'is_student': 'false',
            },
            content_type="application/json",
        )
        self.assertEqual(User.objects.get(email=response.data['email']).id, User.objects.get(id=self.user.id).id)

    def test_delete_user_view(self):
        url = reverse(
            'authentication:crud',
            kwargs={'pk': str(self.user.id)}
        )
        response = self.client.delete(url)

        try:
            User.objects.get(id=self.user.id)
        except User.DoesNotExist:
            self.assertEqual(response.status_code, HTTPStatus.ACCEPTED)
