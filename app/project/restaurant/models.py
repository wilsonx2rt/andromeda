"""DOCSTRING."""
from django.db import models
from django.conf import settings

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


class Category(models.Model):
    name = models.CharField(
        verbose_name='category',
        max_length=100,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Restaurant(models.Model):
    COUNTRIES_CHOICES = (
        ('Switzerland', 'Switzerland'),
        ('Germany', 'Germany'),
        ('France', 'France')
    )

    user = models.ForeignKey(
        verbose_name='creator',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    name = models.CharField(
        verbose_name='restaurant_name',
        max_length=40,
    )

    category = models.ForeignKey(
        verbose_name='category',
        to='restaurant.Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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
        related_name='like',
        blank=True
    )

    unique_together = [
        ("user", "restaurant"),
    ]

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

    def __str__(self):
        return self.text_content+'...'


class Like(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='like_user'
    )

    review = models.ForeignKey(
        verbose_name='review',
        to='restaurant.RestaurantReview',
        on_delete=models.CASCADE,
        related_name='like_user'
    )

    class Meta:
        unique_together = [
            ('user', 'review')
        ]

    def __str__(self):
        return 'Like!'


class LikeComment(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='like_user_c'
    )

    comment = models.ForeignKey(
        verbose_name='comment',
        to='restaurant.Comment',
        on_delete=models.CASCADE,
        related_name='like_user_c'
    )

    class Meta:
        unique_together = [
            ('user', 'comment')
        ]

    def __str__(self):
        return 'Like!'
