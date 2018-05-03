from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.models import Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'review', 'text_content', 'date_created', 'date_modified']
        read_only_fields = ['user', 'review']

    def create(self, validated_data):
        return Comment.objects.create(
            **validated_data,
            review=self.context.get('request').review,
            user=self.context.get('request').user,
        )


# class LikeSerializer(serializers.Serializer):
#
#     def create(self, comment):
#         return Like.objects.create(
#             comment=comment,
#             user=self.context.get('request').user,
#         )
