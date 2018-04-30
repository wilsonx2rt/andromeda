from django.db import models
from django.conf import settings

class User(models.Model):

    user_ID = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_IDs",
    )

    username = models.OneToOneField(
        verbose_name = 'username',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'usernames'
    )

    def code_generator():
        return random.randint(10000, 99999)

    registration_code = models.CharField(
        verbose_name='registration_code',
        max_length=15,
        unique=True,
        default=code_generator
    )

    first_name = models.CharField(
        verbose_name = 'firstname',
        max_length = 40,
        default = ''
    )



#     def __str__(self):
#         return f"User: {self.user}\n"
#
