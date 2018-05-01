from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.models import Restaurant

User = get_user_model()


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'category', 'city']
        read_only_fields = ['id', 'name', 'category', 'city']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            **data
        }

    def create(self, validated_data):
        return Restaurant.objects.create(
            **validated_data,
            restaurant=self.context.get('request').restaurant,
        )
