from . import models
from rest_framework import serializers
from academy.serializers import SemesterSerializer


class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ["student"]
        model = models.NextOfKin

    def create(self, validated_data):
        validated_data["student"] = self.context["request"].user
        return super().create(validated_data)


class StudentRegistrationSerializer(serializers.ModelSerializer):
    calculate_gpa = serializers.DecimalField(
        read_only=True, max_digits=5, decimal_places=2
    )

    class Meta:
        exclude = ["student"]
        model = models.StudentRegistration
        read_only_fields = ["current_step", "is_completed"]

    def create(self, validated_data):
        validated_data["student"] = self.context["request"].user
        return super().create(validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    registration = StudentRegistrationSerializer(read_only=True)
    academic_year = serializers.CharField(source="academic_year.name", read_only=True)

    class Meta:
        exclude = ["student"]
        model = models.Payment

    def create(self, validated_data):
        validated_data["student"] = self.context["request"].user
        return super().create(validated_data)


class RegisteredCourseSerializer(serializers.ModelSerializer):

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
