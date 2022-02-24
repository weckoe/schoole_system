from rest_framework import serializers

from api.models import Assignment

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
    pk = serializers.CharField(required=True) 

    class Meta:
        model = Assignment
        fields = (
            'title',
            'pk',
        )

    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data['pk'])
        assignment = Assignment.objects.create(
            title=validated_data['title'],
            teacher=user,
        )

        assignment.save()
        
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
