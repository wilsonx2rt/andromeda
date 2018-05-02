from django.db import models
from django.conf import settings

from project.restaurant.helpers import code_generator


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )

    registration_code = models.CharField(
        verbose_name='registration_code',
        max_length=15,
        unique=True,
        default=code_generator,
        blank=True
    )

    location = models.CharField(
        verbose_name='location',
        max_length=58,
        blank=True
    )

    phone = models.CharField(
        verbose_name='phone_number',
        max_length=50,
        blank=True
    )

    things_I_love = models.CharField(
        verbose_name='things_I_love',
        max_length=50,
        blank=True
    )

    description = models.CharField(
        verbose_name='description',
        max_length=3000,
        blank=True
    )

    joined_date = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    profile_picture = models.ImageField(
        verbose_name='profile_picture',
        upload_to='../profile_pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
