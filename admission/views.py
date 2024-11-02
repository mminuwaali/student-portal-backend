from . import models, serializers
from rest_framework import viewsets, response
from rest_framework.decorators import action


class NextOfKinViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NextOfKinSerializer

    def get_queryset(self):
        return models.NextOfKin.objects.filter(student=self.request.user)


class RegisteredCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RegisteredCourse.objects.all()
    serializer_class = serializers.RegisteredCourseSerializer


class RegisteredSemesterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RegisteredSemester.objects.all()
    serializer_class = serializers.RegisteredSemesterSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(student=self.request.user)
        fk = self.kwargs.get("academic_year_pk")

        return queryset.filter(semester__academic_year__id=fk) if fk else queryset


class StudentRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentRegistrationSerializer

    def get_queryset(self):
        return models.StudentRegistration.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    @action(detail=True)
    def courses(self, request, pk=None):
        registration = self.get_object()
        courses = models.CourseRegistration.objects.filter(
            student_registration=registration
        )
        serializer = serializers.CourseRegistrationSerializer(courses, many=True)
        return response.Response(serializer.data)


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PaymentSerializer

    def get_queryset(self):
        return models.Payment.objects.filter(student=self.request.user)

    @action(detail=True, methods=["post"])
    def verify(self, request, pk=None):
        payment = self.get_object()
        # Add payment verification logic here
        return response.Response({"status": "verification initiated"})
