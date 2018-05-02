from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    queryset = RestaurantReview.objects.all()

    def list(self, request, *args, **kwargs):
        reviews = self.get_object()
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)