from . import models, serializers
from rest_framework import views, response, viewsets, permissions


class UserView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(request.user)
        return response.Response(serializer.data)
