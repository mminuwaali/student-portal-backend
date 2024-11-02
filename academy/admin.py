from . import models
from django.contrib import admin


class DepartmentInline(admin.TabularInline):
    extra, model = 0, models.Department


class SemesterInline(admin.TabularInline):
    extra, model = 0, models.Semester
    fields = ["name", "start_date", "end_date"]


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    inlines = [DepartmentInline]
    list_display = ["name", "code", "created_at", "updated_at"]


# @admin.register(models.Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     search_fields = ["name"]
#     list_filter = ["faculty"]
#     list_display = ["name", "code", "faculty", "created_at", "updated_at"]


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["lecturer", "unit"]
    list_display = ["name", "unit", "lecturer", "created_at", "updated_at"]


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(models.AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    inlines = [SemesterInline]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(models.RegistrationPeriod)
class RegistrationPeriodAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["academic_year"]
    list_display = ["name", "academic_year", "start_date", "end_date"]


# @admin.register(models.Semester)
# class SemesterAdmin(admin.ModelAdmin):
#     search_fields = ["name"]
#     list_filter = ["academic_year"]
#     list_display = ["name", "academic_year", "start_date", "end_date"]
