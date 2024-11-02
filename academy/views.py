from django.utils import timezone
from . import models, serializers
from rest_framework import viewsets


class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        fk = self.kwargs.get("faculty_pk")

        return queryset.filter(faculty__id=fk) if fk else queryset


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer


class AcademicYearViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.AcademicYear.objects.all()
    serializer_class = serializers.AcademicYearSerializer


class RegistrationPeriodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RegistrationPeriod.objects.all()
    serializer_class = serializers.RegistrationPeriodSerializer

    def get_queryset(self):
        now = timezone.now
        queryset = super().get_queryset()

        return queryset.filter(start_date__lte=now, end_date__gte=now)


class SemesterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Semester.objects.all()
    serializer_class = serializers.SemesterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        fk = self.kwargs.get("academic_year_pk")

        return queryset.filter(academic_year__id=fk) if fk else queryset
