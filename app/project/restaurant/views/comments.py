from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from project.exeptions import LikeDoesNotExist
from project.restaurant.models import RestaurantReview, Comment, LikeComment
from project.restaurant.serializers.comments import CommentSerializer


class NewCommentView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = RestaurantReview.objects.all()

    def post(self, request):
        review = self.get_object()
        request.review = review
        serializer = self.get_serializer(
            data=request.data,
            context={
                'request': request,
            }
        )
        serializer.is_valid(raise_exception=True)
        comment = serializer.create(serializer.validated_data)
        return Response(CommentSerializer(comment).data)


class GetEditDeleteCommentView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self):
        comment = self.get_object()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def post(self, request):
        comment = self.get_object()
        serializer = self.get_serializer(
            comment,
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(CommentSerializer(comment).data)

    def delete(self, request, **kw):
        comment = self.get_object()
        comment.delete()
        return Response('Comment deleted')


class AllCommentsByUserView(APIView):
    """
    deal with case in which user does not exist
    """

    def get(self, request, user_id):
        comments = Comment.objects.filter(user_id=user_id)
        return Response(CommentSerializer(comments, many=True).data)


class LikeUnlikeCommentView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def post(self, request, **kwargs):
        comment = self.get_object()
        user = request.user
        like, created = LikeComment.objects.get_or_create(user=user, comment=comment)
        return Response(created)

    def delete(self, request, **kwargs):
        comment = self.get_object()
        user = request.user
        try:
            like = LikeComment.objects.get(user=user, comment=comment)
        except LikeDoesNotExist:
            return Response('No item to be deleted!')
        like.delete()
        return Response('OK!')
