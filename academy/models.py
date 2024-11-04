from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Faculty(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name.title()


class Department(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    faculty = models.ForeignKey(Faculty, models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name.title()


class Course(models.Model):
    unit = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    lecturer = models.ForeignKey(User, models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, blank=True,null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Level(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "year"
        verbose_name_plural = "years"

    def __str__(self):
        return self.name


class RegistrationPeriod(models.Model):
    end_date = models.DateField()
    start_date = models.DateField()
    description = models.TextField(default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)
    academic_year = models.ForeignKey(AcademicYear, models.CASCADE)

    class Meta:
        verbose_name = "period"
        ordering = ["academic_year"]
        verbose_name_plural = "periods"

    def __str__(self):
        return f"Registration period for {self.academic_year}"


class Semester(models.Model):
    end_date = models.DateField()
    start_date = models.DateField()
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    academic_year = models.ForeignKey(AcademicYear, models.CASCADE)

    class Meta:
        ordering = ["academic_year", "name"]
        unique_together = ["name", "academic_year"]

    def __str__(self):
        return f"{self.name} - {self.academic_year}"
