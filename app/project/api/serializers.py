
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers
from project.api.models import User, Like, UserProfile, FriendRequest

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='Email address'
    )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            return value

    def send_registration_email(self, email, code):
        message = EmailMessage(
            subject='Social feed registration',
            body=f"This is your registration code: {code}",
            to=[email],

        )
        message.send()
