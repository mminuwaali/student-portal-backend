from . import models
from rest_framework import serializers
from account.serializers import UserSerializer


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Faculty


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ["faculty"]
        model = models.Department


class CourseSerializer(serializers.ModelSerializer):
    lecturer = UserSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = models.Course


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Level


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.AcademicYear


class RegistrationPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = models.RegistrationPeriod


class SemesterSerializer(serializers.ModelSerializer):
    academic_year = serializers.CharField(source="academic_year.name", read_only=True)
    class Meta:
        exclude = []
        model = models.Semester
