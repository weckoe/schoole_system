from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.core.files.images import get_image_dimensions

from authentication.models import User

MAX_UPLOAD_PHOTO_WIDTH = 200
MAX_UPLOAD_PHOTO_HEIGHT = 200


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(
            write_only=True, 
            required=True,
            validators=[validate_password]
    )
    
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "is_student",
        )

    def validate(self, validated_data):
        if validated_data["password"] != validated_data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return validated_data

    def validate_image(self, image):
        image_width, image_height = get_image_dimensions(image)

        if image_width != MAX_UPLOAD_PHOTO_WIDTH or image_height != MAX_UPLOAD_PHOTO_HEIGHT:
            raise serializers.ValidationError(
                f'Image resolution must be {MAX_UPLOAD_PHOTO_WIDTH}x{MAX_UPLOAD_PHOTO_HEIGHT}'
            )
        return image

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_student=validated_data["is_student"],
        )        
        user.set_password(validated_data["password"])
        user.save()

        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "is_student")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.email = validated_data["email"]
        instance.is_student = validated_data["is_student"]

        instance.save()

        return instance


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                "email",
                "id",
                "first_name",
                "last_name",
                "is_student",
        )


