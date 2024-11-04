from . import models
from rest_framework import serializers
from academy.serializers import LevelSerializer, CourseSerializer, SemesterSerializer


class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ["student"]
        model = models.NextOfKin

    def create(self, validated_data):
        validated_data["student"] = self.context["request"].user
        return super().create(validated_data)


class StudentRegistrationSerializer(serializers.ModelSerializer):
    level_data = LevelSerializer(source="level", read_only=True)
    calculate_gpa = serializers.DecimalField(
        read_only=True, max_digits=5, decimal_places=2
    )

    class Meta:
        exclude = ["student"]
        model = models.StudentRegistration
        read_only_fields = ["current_step", "is_completed"]

    def validate(self, attrs):
        user = self.context["request"].user
        if models.StudentRegistration.objects.filter(
            student=user, level=attrs["level"], academic_year=attrs["academic_year"]
        ).exists():
            raise serializers.ValidationError(
                "You have already registered for this level and academic year"
            )
        return attrs

    def create(self, validated_data):
        validated_data["student"] = self.context["request"].user
        return super().create(validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    academic_year_data = serializers.CharField(source="academic_year.name", read_only=True)
    registration_data = StudentRegistrationSerializer(read_only=True, source="registration")

    class Meta:
        exclude = ["student"]
        model = models.Payment

    def create(self, validated_data):
        validated_data["student"] = self.context["request"].user
        return super().create(validated_data)


class RegisteredCourseSerializer(serializers.ModelSerializer):
    course_data = CourseSerializer(source="course", read_only=True)

    class Meta:
        fields = "__all__"
        model = models.RegisteredCourse


class RegisteredSemesterSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    semester = SemesterSerializer(read_only=True)
    gpa = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)
    cgpa = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)

    class Meta:
        fields = "__all__"
        model = models.RegisteredSemester

    def get_courses(self, model):
        courses = models.RegisteredCourse.objects.filter(semester=model)
        return RegisteredCourseSerializer(courses, many=True).data
