from rest_framework import serializers

from api.models import Assignment, Choice, Question

from authentication.models import User

from django.shortcuts import get_object_or_404


class ReadAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'title',
            'teacher',
            'id',
        )


class CreateAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'title',
            'teacher',
        )

    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data['teacher'].id)
        assignment = Assignment.objects.create(
            title=validated_data['title'],
            teacher=user,
        )

        return assignment


class UpdateAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'title',
            'teacher',
        )

    def patch(self, instance, validated_data):
        user = get_object_or_404(User, id=validated_data['teacher'])
        instance.title = validated_data['title']
        instance.teacher = user
        instance.save()

        return instance


class ReadChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'title',
            'id',
        )


class CreateChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            'title',
        )

    def create(self, validated_data):
        assignment = Choice.objects.create(
            title=validated_data['title'],
        )

        return assignment


class UpdateChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            'title',
        )

    def patch(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()

        return instance


class ReadQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'choices',
            'answer',
            'assignment',
            'order',
        )


class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question',
            'choices',
            'answer',
            'assignment',
            'order',
        )

    def create(self, validated_data):
        question = Question.objects.create(
            question=validated_data['question'],
            answer=validated_data['answer'],
            assignment=validated_data['assignment'],
            order=validated_data['order'],
        )
        
        for k in validated_data['choices']:
            question.choices.add(k)

        return question


class UpdateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question',
            'choices',
            'answer',
            'assignment',
            'order',
        )

    def patch(self, instance, validated_data):
        instance.question = validated_data['question']
        instance.answer = validated_data['answer']
        instance.assignment = validated_data['assignment']
        instance.order = validated_data['order']
          

        for k in validated_data['choices']:
            instance.choices.add(k)

        instance.save()

        return instance
