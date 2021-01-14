from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        """
        メタ情報
        """
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {
            "write_only": True,  # 書き込みのみ許可
            "required": True,  # 必須
        }}

    def create(self, validated_data):
        """
        user作成時処理
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TaskSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        """
        メタ情報
        """
        model = Task
        fields = ["id", "title", "created_at", "updated_at"]
