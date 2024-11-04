from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("user/", views.UserView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("change-password/", views.ChangePasswordView.as_view()),
]
