from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.restaurant.models import Comment, RestaurantReview
from project.restaurant.serializers.comment import CommentSerializer
from project.restaurant.serializers.like import LikeSerializer


class GetCommentsCurrentUser(APIView):

    def get(self, request):
        comments = Comment.objects.filter(user=request.user)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class GetCommentsUser(GenericAPIView):

    serializer_class = CommentSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        print(user)
        comments = Comment.objects.filter(user=user)
        return Response(self.get_serializer(comments, many=True).data)