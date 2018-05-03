from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.state import User

from project.restaurant.models import Restaurant, RestaurantReview
from project.restaurant.serializers.restaurantreview import RestaurantReviewSerializer
from project.restaurant.permissions import IsOwnerOrReadOnly


class NewRestaurantReview(ListAPIView):
    serializer_class = RestaurantReviewSerializer
    queryset = Restaurant.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RestaurantsReviewOneRestaurantView(ListAPIView):
    serializer_class = RestaurantReviewSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    queryset = Restaurant.objects.all()

    def list(self, request, *args, **kwargs):
        restaurant = self.get_object()
        reviews = RestaurantReview.objects.filter(restaurant=restaurant)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)


class RestaurantUserReviews(ListAPIView):
    serializer_class = RestaurantReviewSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user = self.get_object()
        reviews = RestaurantReview.objects.filter(user=user)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)


class ReviewsAllPurpose(ListAPIView):
    serializer_class = RestaurantReviewSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    queryset = RestaurantReview.objects.all()

    def get(self, request, **kwargs):
        review = self.get_object()
        return Response(self.get_serializer(review).data)

    def post(self, request, **kwargs):
        review = self.get_object()
        serializer = self.get_serializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        finalReview = serializer.save()
        return Response(self.get_serializer(finalReview).data)

    def delete(self, request, **kwargs):
        review = self.get_object()
        review.delete()
        return Response('OK!')
