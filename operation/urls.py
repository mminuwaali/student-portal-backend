from . import views
from django.urls import path, include
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("timetable", views.TimeTableViewSet, "timetable")
router.register("attendance", views.AttendanceViewSet, "attendance")

urlpatterns = [
    path("", include(router.urls)),
]
