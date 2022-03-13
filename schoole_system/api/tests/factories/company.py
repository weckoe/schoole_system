import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'authentication.User'

    id = factory.Faker('uuid4')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_student = True
    password = factory.PostGenerationMethodCall('set_password', 'faker432143124')


class AssignmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.Assignment'

    title = factory.Faker('word')


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.Choice'

    title = factory.Faker('word')


user_factory = UserFactory()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.Question'

    question = factory.Faker('word')
    order = '123'
