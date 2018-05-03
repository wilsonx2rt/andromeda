from rest_framework import serializers

from project.restaurant.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']