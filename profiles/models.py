from django.db import models
from django.contrib.auth import get_user_model
from academy.models import Level, Faculty, Department, AcademicYear

User = get_user_model()


class AcademicProfile(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.OneToOneField(User, models.CASCADE)
    department = models.ForeignKey(Department, models.CASCADE)
    faculty = models.ForeignKey(Faculty, models.CASCADE, editable=False)
    current_academy = models.OneToOneField(
        "AcademicHistory", models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        self.faculty = self.department.faculty
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - Level {self.current_academy.level if self.current_academy else 'N/A'}"


class AcademicHistory(models.Model):
    level = models.ForeignKey(Level, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    academic_year = models.ForeignKey(AcademicYear, models.CASCADE)
    academic_profile = models.ForeignKey(AcademicProfile, models.CASCADE)

    class Meta:
        ordering = ["-academic_year"]
        verbose_name_plural = "Academic histories"
        unique_together = ["academic_year", "academic_year"]

    def __str__(self):
        return f"{self.academic_profile.student} - {self.academic_year} ({self.level})"
