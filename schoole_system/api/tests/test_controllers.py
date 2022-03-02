import http
from uuid import UUID

from django.test import TestCase, Client
from django.urls import reverse

from api.models import Assignment, Choice, Question
from authentication.models import User


class TestAssignmentView(TestCase):
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

        self.assignment = Assignment.objects.create(
            id=2,
            title='test',
            teacher=self.user,
        )

    def test_assignment_list_view(self):
        url = reverse('api:assignment-list')
        response = self.client.get(url)
        self.assertEqual(response.data['results'][0]['teacher'], self.user.id)

    def test_get_single_assignment_view(self):
        url = reverse(
            'api:assignment-crud',
            kwargs={'pk': '2'}
        )
        response = self.client.get(url)
        self.assertEqual(response.data['teacher'], self.user.id)

    def test_assignment_create_view(self):
        url = reverse('api:assignment-list')
        response = self.client.post(
            url,
            data={
                'title': 'post test',
                'teacher': str(self.user.id),
            }
        )
        self.assertEqual(response.data, 'post test')

    def test_assignment_update_view(self):
        url = reverse(
            'api:assignment-crud',
            kwargs={
                'pk': '2',
            }
        )
        response = self.client.patch(
            url,
            data={
                'title': 'updated post',
                'teacher': '4b6ce8b2-789d-46fc-822f-7bbb4ee3956f',
            },
            content_type='application/json'
        )
        self.assertEqual(Assignment.objects.get(id=2).title, 'updated post')

    def test_assignment_delete_view(self):
        url = reverse(
            'api:assignment-crud',
            kwargs={
                'pk': '2',
            }
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, http.HTTPStatus.NO_CONTENT)


class TestChoiceView(TestCase):
    def setUp(self):
        self.client = Client()

        self.choice = Choice.objects.create(
            id=2,
            title='test',
        )

    def test_choice_list_view(self):
        url = reverse('api:choice-list')
        response = self.client.get(url)
        self.assertEqual(response.data['results'][0]['title'], self.choice.title)

    def test_get_single_choice_view(self):
        url = reverse(
                'api:choice-crud',
                kwargs={
                    'pk': '2',
                    }
        )
        response = self.client.get(url)
        self.assertEqual(response.data['id'], self.choice.id)

    def test_create_choice_view(self):
        url = reverse('api:choice-list')
        response = self.client.post(
                url,
                data={
                    'title': 'test choice'
                    },
        )
        self.assertEqual(response.data, 'test choice')

    def test_update_choice_view(self):
        url = reverse(
                'api:choice-crud',
                kwargs={
                    'pk': '2',
                    }
        )
        response = self.client.patch(
                url,
                data = {
                    'title': 'patchtest' 
                    }, 
                content_type='application/json'
        )
        self.assertEqual(response.data, 'patchtest')

    def test_delete_choice_view(self):
        url = reverse(
                'api:choice-crud',
                kwargs={
                    'pk': '2',
                    }
        )
        response = self.client.delete(
                    url,
                    )
        self.assertEqual(response.status_code, http.HTTPStatus.NO_CONTENT)


class TestQuestionView(TestCase):
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

        self.choices=Choice.objects.create(
                id=1,
                title='single choice'
        )

        self.assignment = Assignment.objects.create(
            title = 'test assignment',
            teacher= self.user,
                    ) 
                
        self.question = Question.objects.create(
            question='Test Question',
            answer=self.choices,
            assignment=self.assignment,
            order=123,
        )
        self.question.choices.add(self.choices)
        
    def test_question_list_view(self):
        url = reverse('api:question-list') 
        response = self.client.get(url)
        self.assertEqual(response.data['results'][0]['question'], self.question.question)

    def test_single_question_view(self):
        url = reverse(
                'api:question-crud',
                kwargs={
                    'pk': str(self.question.id),
                    }
        )
        response = self.client.get(url)
        self.assertEqual(response.data['question'], self.question.question)

    def test_question_create_view(self):
        url = reverse(
                'api:question-list'
                )
        
        response = self.client.post(
                url,
                data={
                    'question': 'Second Test',
                    'choices': str(self.choices.id),
                    'answer': str(self.choices.id),
                    'assignment': str(self.assignment.id),
                    'order': '432',
                    }
                )
        self.assertEqual(response.data, 'Second Test')
        self.assertEqual(
                Question.objects.get(question='Second Test').question, 
                'Second Test')

    def test_update_question_view(self):
        url = reverse(
                'api:question-crud',
                kwargs={
                    'pk': str(self.question.id)
                    }
            )
        response = self.client.patch(
                url,
                data={
                    "id": str(self.question.id),
                    "question": "New Test",
                    "choices": [
                        str(self.choices.id),
                    ],
                    "answer": str(self.choices.id),
                    "assignment": str(self.assignment.id),
                    "order": 123
                },
                content_type='application/json',
        )
        
        self.assertEqual(response.data, 'New Test')
    
    def test_delete_question_view(self):
        url = reverse(
                'api:question-crud',
                kwargs={
                    'pk': str(self.question.id),
                    }
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, http.HTTPStatus.NO_CONTENT)
