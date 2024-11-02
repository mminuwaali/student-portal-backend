from . import models
from django.contrib import admin


class RegisteredCourseInline(admin.StackedInline):
    extra, model = 0, models.RegisteredCourse


class RegisteredSemesterInline(admin.StackedInline):
    extra, model = 0, models.RegisteredSemester


@admin.register(models.NextOfKin)
class NextOfKinAdmin(admin.ModelAdmin): ...


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin): ...


@admin.register(models.StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    ...
    # inlines = [RegisteredSemesterInline]


@admin.register(models.RegisteredSemester)
class RegisteredSemesterAdmin(admin.ModelAdmin):
    inlines = [RegisteredCourseInline]


@admin.register(models.RegisteredCourse)
class RegisteredCourseAdmin(admin.ModelAdmin): ...
