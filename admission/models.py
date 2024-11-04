from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator as Max
from academy.models import Level, Course, Semester, AcademicYear

User = get_user_model()


class NextOfKin(models.Model):
    address = models.TextField()
    email = models.EmailField(blank=True)
    full_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student}: {self.full_name} - {self.relationship}"


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ("FAILED", "Failed"),
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("PROCESSING", "Processing"),
    ]

    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    registration = models.OneToOneField("StudentRegistration", models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, models.CASCADE, editable=False)
    status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default="PENDING"
    )

    def __str__(self):
        return f"{self.student.username} - {self.reference}"

    def save(self, *args, **kwargs):
        self.academic_year = self.registration.academic_year
        super().save(*args, **kwargs)


class StudentRegistration(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    level = models.ForeignKey(Level, models.CASCADE)
    student = models.ForeignKey(User, models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    academic_year = models.ForeignKey(AcademicYear, models.CASCADE)

    def __str__(self):
        return f"{self.student.username} - {self.academic_year.name}"

    def save(self, *args, **kwargs):
        self.create_registered_semesters()
        super().save(*args, **kwargs)

    @property
    def calculate_gpa(self):
        semesters = self.academic_year.semester_set.all()

        return sum(
            [
                i.cgpa
                for i in RegisteredSemester.objects.filter(
                    student=self.student, semester__in=semesters
                )
            ]
        )

    def create_registered_semesters(self):
        semesters = self.academic_year.semester_set.all()

        RegisteredSemester.objects.bulk_create(
            [RegisteredSemester(student=self.student, semester=i) for i in semesters]
        )

    class Meta:
        unique_together = ["student", "academic_year"]

    def __str__(self):
        return f"{self.student} - {self.academic_year.name}"


class RegisteredSemester(models.Model):
    student = models.ForeignKey(User, models.CASCADE)
    semester = models.ForeignKey(Semester, models.CASCADE)
    courses = models.ManyToManyField(Course, through="RegisteredCourse", blank=True)

    def __str__(self):
        return f"{self.student} - {self.semester.name}  - {self.semester.academic_year}"

    @property
    def gpa(self):
        result = self.registeredcourse_set.aggregate(
            total_score=models.Sum(
                models.F("course__unit") * models.F("score") / 100 * 5
            ),
            total_units=models.Sum("course__unit"),
        )

        total_score = float(result["total_score"] or 0)
        total_units = float(result["total_units"] or 0)

        return total_score / total_units if total_units > 0 else 0

    @property
    def cgpa(self):
        result = RegisteredCourse.objects.filter(
            semester__student=self.student
        ).aggregate(
            total_units=models.Sum("course__unit"),
            total_score=models.Sum(
                models.F("course__unit") * models.F("score") / 100 * 5
            ),
        )

        total_score = float(result["total_score"] or 0)
        total_units = float(result["total_units"] or 0)

        return total_score / total_units if total_units > 0 else 0


class RegisteredCourse(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    semester = models.ForeignKey(RegisteredSemester, models.CASCADE)
    score = models.DecimalField(
        default=0, max_digits=5, decimal_places=2, validators=[Max(100.0)]
    )

    def __str__(self):
        return f"{self.course.code} - {self.semester.student}"

    @property
    def weighted_score(self):
        return self.grade_point * self.course.unit

    @property
    def grade_point(self):
        if self.score is None:
            return 0
        elif self.score >= 70:
            return 5.0
        elif self.score >= 60:
            return 4.0
        elif self.score >= 50:
            return 3.0
        elif self.score >= 45:
            return 2.0
        else:
            return 0.0
