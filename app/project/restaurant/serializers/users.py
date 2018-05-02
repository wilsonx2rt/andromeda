from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.serializers.me import UserProfileSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_profile']
        read_only_fields = fields
