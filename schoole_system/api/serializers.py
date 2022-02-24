from rest_framework import serializers

from api.models import Assignment

from authentication.models import User


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
        assignment = Assignment.objects.create(
            title=validated_data['title'],
            teacher=User.objects.get(id=validated_data['pk']),
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
        instance.title = validated_data['title']
        instance.teacher = User.objects.get(id=validated_data['teacher'])
        instance.save()

        return instance
