from django.db import models
from django.conf import settings

from .helpers import code_generator

PRICING_CHOICES = (
    ('$', 'very cheap'),
    ('$$', 'cheap'),
    ('$$$', 'medium'),
    ('$$$$', 'expensive'),
    ('$$$$$', 'very expensive'),
)

RATING_CHOICES = (
    ('*', 'Poor'),
    ('**', 'Acceptable'),
    ('***', 'Alright!'),
    ('****', 'Good'),
    ('*****', 'Excellent'),
)


# class UserProfile(models.Model):
#
#     user = models.OneToOneField(
#         verbose_name='user_name',
#         to=settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='user_name'
#     )
#
#     registration_code = models.CharField(
#         verbose_name='registration_code',
#         max_length=15,
#         unique=True,
#         default=code_generator,
#         blank=True
#     )
#
#     # first_name = models.CharField(
#     #     verbose_name='first_name',
#     #     max_length=40,
#     #     default='',
#     # )
#     #
#     # last_name = models.CharField(
#     #     verbose_name='last_name',
#     #     max_length=130,
#     #     default='',
#     # )
#
#     email = models.CharField(
#         verbose_name='email_address',
#         max_length=254,
#         unique=True
#     )
#
#     location = models.CharField(
#         verbose_name='location',
#         max_length=58,
#         blank=True
#     )
#
#     phone = models.CharField(
#         verbose_name='phone_number',
#         max_length=50,
#         blank=True
#     )
#
#     things_I_love = models.CharField(
#         verbose_name='things_I_love',
#         max_length=50,
#         blank=True
#     )
#
#     description = models.CharField(
#         verbose_name='description',
#         max_length=3000,
#         blank=True
#     )
#
#     joined_date = models.DateTimeField(
#         verbose_name='created',
#         auto_now_add=True
#     )
#
#     profile_picture = models.ImageField(
#         upload_to='../profile_pictures/',
#         blank=True,
#         null=True
#     )
#
#     def __str__(self):
#         return self.user

class Restaurant(models.Model):
    COUNTRIES_CHOICES = (
        ('Switzerland', 'Switzerland'),
        ('Germany', 'Germany'),
        ('France', 'France')
    )

    name = models.CharField(
        verbose_name='restaurant_name',
        max_length=40,
    )

    category = models.CharField(
        verbose_name='category',
        max_length=20,
        blank=True
    )

    country = models.CharField(
        verbose_name='country',
        max_length=58,
        choices=COUNTRIES_CHOICES,
    )

    street = models.CharField(
        verbose_name='street',
        max_length=50
    )

    city = models.CharField(
        verbose_name='city',
        max_length=58
    )

    zip = models.CharField(
        verbose_name='zip_code',
        max_length=10
    )

    website = models.CharField(
        verbose_name='website',
        max_length=100,
        blank=True
    )

    phone = models.CharField(
        verbose_name='phone',
        max_length=100,
        blank=True
    )

    email = models.CharField(
        verbose_name='email',
        max_length=100,
        blank=True
    )

    opening_hours = models.TextField(
        verbose_name='opening_hours',
        max_length=1200
    )

    price_level = models.CharField(
        verbose_name='price_level',
        max_length=5,
        choices=PRICING_CHOICES,
    )

    image = models.ImageField(
        upload_to='restaurant_pictures',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class RestaurantReview(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='users',
        null=True
    )

    restaurant = models.ForeignKey(
        verbose_name='restaurant',
        to=Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_name',
        null=True
    )

    rating = models.CharField(
        verbose_name='grade',
        choices=RATING_CHOICES,
        max_length=10
    )

    text_content = models.TextField(
        verbose_name='text_content',
        max_length=300
    )

    date_created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    date_modified = models.DateTimeField(
        verbose_name='date_modified',
    )

    like = models.ManyToManyField(
        verbose_name='like',
        to=settings.AUTH_USER_MODEL,
        related_name='user',
        blank=True
    )

    unique_together = (
        ("user", "restaurant"),
    )

    def __str__(self):
        return self.text_content[:16]+'...'


class Comment(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_user'
    )

    review = models.ForeignKey(
        verbose_name='review',
        to='restaurant.RestaurantReview',
        on_delete=models.CASCADE,
        related_name='comment_user'
    )

    text_content = models.TextField(
        verbose_name='text_content',
    )

    date_created = models.DateTimeField(
        verbose_name='date_created',
        auto_now_add=True
    )

    date_modified = models.DateTimeField(
        verbose_name='date_modified',
    )

    # comment_like = models.ManyToManyField(
    #     verbose_name='like_comment',
    #     to='restaurant.RestaurantReview',
    #     related_name='comment',
    #     blank=True
    # )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        unique_together = [
            ('user', 'review'),
        ]

    def __str__(self):
        return self.text_content+'...'
