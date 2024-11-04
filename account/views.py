from . import models, serializers
from rest_framework import views, status, response


class UserView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(request.user)
        return response.Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(
            request.user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(views.APIView):

    def post(self, request):
        confirm = request.data.get("confirm")
        password = request.data.get("password")
        current_password = request.data.get("current")

        if not request.user.check_password(current_password):
            return response.Response(
                {"error": "Invalid current password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if password != confirm:
            return response.Response(
                {"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST
            )

        request.user.set_password(password)
        request.user.save()
        return response.Response(
            {"message": "Password changed successfully"}, status=status.HTTP_200_OK
        )
