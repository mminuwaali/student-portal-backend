from django.db import models
from academy.models import Course, Semester
from django.contrib.auth import get_user_model

User = get_user_model()
WEEKDAYS = [
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
]


class TimeTable(models.Model):
    end_time = models.TimeField()
    start_time = models.TimeField()
    venue = models.CharField(max_length=100)
    weekday = models.IntegerField(choices=WEEKDAYS)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    semester = models.ForeignKey(Semester, models.CASCADE)

    class Meta:
        unique_together = ["course", "semester", "weekday", "start_time"]

    def __str__(self):
        return f"{self.course} - {self.get_weekday_display()} ({self.start_time} - {self.end_time})"


class Attendance(models.Model):
    is_present = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    timetable = models.ForeignKey(TimeTable, models.CASCADE)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["student", "timetable"]

    def __str__(self):
        return f"{self.student} - {self.timetable.course} ({self.timetable.get_weekday_display()})"
