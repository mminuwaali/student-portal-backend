from . import models
from rest_framework import serializers
from academy.serializers import CourseSerializer


class TimeTableSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    semester = serializers.CharField(read_only=True, source="semester.name")
    weekday = serializers.CharField(read_only=True, source="get_weekday_display")

    class Meta:
        fields = "__all__"
        model = models.TimeTable


class AttendanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    timetable = TimeTableSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = models.Attendance
