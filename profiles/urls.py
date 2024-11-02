from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", views.AcademicProfileViewSet)
router.register("history", views.AcademicHistoryViewSet)

urlpatterns = [path("", include(router.urls))]
