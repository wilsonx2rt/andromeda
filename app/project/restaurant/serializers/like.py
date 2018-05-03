from rest_framework import serializers

from project.restaurant.models import Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'name', 'country', 'street', 'city', 'zip', 'opening_hours', 'price_level']
