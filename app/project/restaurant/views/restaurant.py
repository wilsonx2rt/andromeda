from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.restaurant.models import Restaurant, Category
from project.restaurant.serializers.restaurant import RestaurantSerializer, User
from project.restaurant.permissions import IsOwnerOrReadOnly


class RestaurantGetListView(GenericAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def get(self, request):
        queryset = Restaurant.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class RestaurantPostNewView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RestaurantCategoryView(ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        category = self.get_object()
        restaurants = Restaurant.objects.filter(category=category)
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data)


class RestaurantCreatorView(ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user = self.get_object()
        restaurants = Restaurant.objects.filter(user=user)
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data)



class RestaurantGetPostDeleteView(GenericAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def get(self, request, pk):
        queryset = Restaurant.objects.filter(id=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        restaurant = self.get_object()
        serializer = self.get_serializer(restaurant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        restaurant = self.get_object()
        restaurant.delete()
        return Response('OK')
