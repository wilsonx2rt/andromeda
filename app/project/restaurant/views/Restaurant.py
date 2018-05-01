from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.restaurant.models import Restaurant
from project.restaurant.serializers.Restaurant import RestaurantSerializer
from project.restaurant.permissions import IsOwnerOrReadOnly


class RestaurantGetUpdateDeleteView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def get(self, request, **kwargs):
        restaurant = self.get_object()
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        restaurant = self.get_object()
        restaurant.delete()
        return Response('OK')
