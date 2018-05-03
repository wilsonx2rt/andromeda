
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.restaurant.models import RestaurantReview, Like
from project.restaurant.serializers.like import LikeSerializer
from project.restaurant.serializers.restaurantreview import RestaurantReviewSerializer


class ReviewLikeView(GenericAPIView):
    serializer_class = RestaurantReviewSerializer
    queryset = RestaurantReview.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self):
        restaurant = self.get_object()
        return Response(self.get_serializer(restaurant).data)

    def post(self, request):
        review = self.get_object()
        user = request.user
        like, created = Like.objects.get_or_create(user=user, review=review)
        return Response(created)

    def delete(self, request):
        review = self.get_object()
        try:
            like = Like.objects.get(user=request.user, review=review)
        except Like.DoesNotExist:
            raise ValidationError('blablabala, you suck')
        like.delete()
        return Response('OK!')


class GetLikesView(APIView):

    def get(self, request):
        reviews = RestaurantReview.objects.filter(like_user__user=request.user)
        serializer = RestaurantReviewSerializer(reviews, many=True)
        return Response(serializer.data)

