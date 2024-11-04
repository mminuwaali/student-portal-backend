from . import models
from rest_framework import serializers
from academy.serializers import LevelSerializer,AcademicYearSerializer


class AcademicHistorySerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)
    academic_year = AcademicYearSerializer(read_only=True)

    class Meta:
        exclude = ["academic_profile"]
        model = models.AcademicHistory


class AcademicProfileSerializer(serializers.ModelSerializer):
    faculty = serializers.CharField(source="faculty.name")
    current_academy = AcademicHistorySerializer(read_only=True)
    department = serializers.CharField(source="department.name")

    class Meta:
        exclude = ["student"]
        model = models.AcademicProfile
