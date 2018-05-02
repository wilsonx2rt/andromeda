from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.models import RestaurantReview


class RestaurantReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = RestaurantReview
        fields = ['id', 'user', 'restaurant', 'rating', 'text_content', 'date_modified']