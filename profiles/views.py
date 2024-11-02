from . import models, serializers
from rest_framework import viewsets


class AcademicProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.AcademicProfile.objects.all()
    serializer_class = serializers.AcademicProfileSerializer

    def get_queryset(self):
        return super().get_queryset().filter(student=self.request.user)


class AcademicHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.AcademicHistory.objects.all()
    serializer_class = serializers.AcademicHistorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(academic_profile__student=self.request.user)
