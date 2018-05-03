from rest_framework import serializers

from project.restaurant.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user', 'review', 'text_content', 'date_created', 'date_modified']
