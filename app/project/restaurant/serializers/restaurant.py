from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.models import Restaurant

User = get_user_model()


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'country', 'street', 'city', 'zip', 'opening_hours', 'price_level']
