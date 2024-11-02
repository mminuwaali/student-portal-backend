from . import models
from django.contrib import admin


@admin.register(models.TimeTable)
class TimeTableAdmin(admin.ModelAdmin): ...


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin): ...
