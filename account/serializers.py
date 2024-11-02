from . import models
from rest_framework import serializers
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    class Meta:
        model = models.User
        extra_kwargs = {"password": {"write_only": True}}
        fields = [
            "id",
            "email",
            "profile",
            "password",
            "username",
            "last_name",
            "first_name",
            "last_login",
        ]
