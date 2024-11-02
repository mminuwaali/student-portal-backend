from . import models
from rest_framework import serializers
from academy.serializers import LevelSerializer


class AcademicHistorySerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)
    academic_year = serializers.CharField(source="academic_year.name")

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
