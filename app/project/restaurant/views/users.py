from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from project.restaurant.serializers.users import UserSerializer

User = get_user_model()


class UserListView(APIView):

    def get(self, request):

        users = User.objects.all()
        query_string = request.query_params.get('search')

        if query_string:
            users = users.filter(
                Q(username__contains=query_string) |
                Q(first_name__contains=query_string) |
                Q(last_name__contains=query_string) |
                Q(email__contains=query_string)
            )
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class GetUserById(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
