from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from project.restaurant.serializers.me import MeSerializer, UserProfileUpdateSerializer

User = get_user_model()


class GetUpdateUserProfileView(GenericAPIView):
    serializer_class = UserProfileUpdateSerializer
    output_serializer = MeSerializer

    def get(self, request, **kwargs):
        return Response(self.output_serializer(request.user).data)

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data, context={
            'request': request
        })
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.output_serializer(user).data)
