from django.utils import timezone
from . import models, serializers
from rest_framework import viewsets
from academy.models import Semester
from admission.models import RegisteredCourse


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AttendanceSerializer

    def get_queryset(self):
        return models.Attendance.objects.filter(student=self.request.user)


class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = models.TimeTable.objects.all()
    serializer_class = serializers.TimeTableSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset
        current_date = timezone.now().date()
        current_weekday = timezone.now().weekday()

        if (
            not hasattr(self.request.user, "academicprofile")
            or not self.request.user.academicprofile.current_academy
        ):
            return []

        current_semesters = Semester.objects.filter(
            end_date__gte=current_date, start_date__lte=current_date
        )
        registered_courses = [
            i.course
            for i in RegisteredCourse.objects.filter(
                semester__semester__in=current_semesters
            )
        ]

        return queryset.filter(
            weekday=current_weekday,
            course__in=registered_courses,
            semester__in=current_semesters,
        )
