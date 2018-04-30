from django.db import models
from django.conf import settings


class User(models.Model):

    user_name = models.OneToOneField(
        verbose_name='user_name',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_names'
    )

    def code_generator(self):
        return random.randint(10000, 99999)

    registration_code = models.CharField(
        verbose_name='registration_code',
        max_length=15,
        unique=True,
        default=code_generator
    )

    # first_name = models.CharField(
    #     verbose_name='first_name',
    #     max_length=40,
    #     default='',
    # )
    #
    # last_name = models.CharField(
    #     verbose_name='last_name',
    #     max_length=130,
    #     default='',
    # )

    email = models.CharField(
        verbose_name='email_address',
        max_length=254,
        unique=True
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
        upload_to='../profile_pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user_name

class Restaurant(models.Model):

    name = models.CharField(
        verbose_name='restaurant_name',
        max_length=40,
    )

    category = models.CharField(
        verbose_name='category',
        max_length=20
    )

    country = models.CharField(
        verbose_name='country',
        max_length=58
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
        max_length=100
    )

    phone = models.CharField(
        verbose_name='phone',
        max_length=100
    )

    email = models.CharField(
        verbose_name='email',
        max_length=100
    )

    opening_hours = models.TextField(
        verbose_name='opening_hours',
        max_length=1200
    )

    price_level = models.CharField(
        verbose_name='price_level',
        max_length=5
    )

    image = models.ImageField(
        upload_to='restaurant_pictures',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class RestaurantReview(models.Model):

    text_content = models.TextField(
        verbose_name='text_content',
        max_length=5
    )

    rating = models.IntegerField(
        verbose_name='rating',
    )

    date_created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    date_modified = models.DateTimeField(
        verbose_name='date_modified',
    )

    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    restaurant = models.OneToOneField(
        verbose_name='restaurant',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="restaurant_name",
    )

    like = models.ManyToManyField(
        verbose_name='like',
        to=settings.AUTH_USER_MODEL,
        related_name='user',
    )

    comments = models.ManyToManyField(
        verbose_name='comments',
        to='Comment'
    )

    def __str__(self):
        return self.rating

class Comment(models.Model):

    user = models.ForeignKey(
        verbose_name='comment_user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_user'
    )

    review = models.ForeignKey(
        verbose_name='comment_review',
        to='api.RestaurantReview',
        on_delete=models.CASCADE,
        related_name='comment_review'
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
    #
    # likes = models.ForeignKey(
    #     verbose_name = 'likes'
    #     to='',
    # )

    def __str__(self):
        return self.text_content