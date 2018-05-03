from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.restaurant.models import Category
from project.restaurant.permissions import IsOwnerOrReadOnly
from project.restaurant.serializers.category import CategorySerializer


class GetCategories(APIView):
    serializer_class = CategorySerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def get(self, request):
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
