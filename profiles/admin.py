from django.forms import ModelForm
from django.http import HttpRequest
from . import models
from django.contrib import admin


class AcademicHistoryInline(admin.TabularInline):
    extra, model = 0, models.AcademicHistory


@admin.register(models.AcademicProfile)
class AcademicProfileAdmin(admin.ModelAdmin):
    search_fields = ["student"]
    inlines = [AcademicHistoryInline]
    list_filter = ["faculty", "department"]
    list_display = ["student", "faculty", "department", "current_academy"]


@admin.register(models.AcademicHistory)
class AcademicHistoryAdmin(admin.ModelAdmin):
    list_filter = ["level", "academic_year", "academic_profile"]
    list_display = ["level", "academic_year", "academic_profile", "created_at"]
