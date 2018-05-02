from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.user.models import UserProfile

User = get_user_model()

class UserProfileUpdateSerializer(serializers.Serializer):
    pass


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['registration_code', 'location', 'phone',
                  'things_I_love', 'description', 'joined_date', 'profile_picture']
        read_only_fields = ['registration_code', 'joined_date']


class MeSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(required=False)
    username = serializers.CharField(
        required=False,
        allow_blank=False,
    )

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError('Username is already taken')
        except User.DoesNotExist:
            return username

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_profile']
        read_only_fields = ['id']
