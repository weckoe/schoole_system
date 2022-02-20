from rest_framework import serializers, status
from rest_framework.response import Response

from django.contrib.auth.password_validation import validate_password
from django.core.files.images import get_image_dimensions

from authentication.models import User

MAX_UPLOAD_PHOTO_WIDTH = 200
MAX_UPLOAD_PHOTO_HEIGHT = 200


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "image",
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
            image=validated_data["image"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def update(self, instance, validated_data):
        print(validated_data)
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.email = validated_data["email"]

        instance.save()

        return instance


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "id",
            "email",
        ]


