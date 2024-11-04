from . import models
from django.db.models import signals
from django.dispatch import receiver
from profiles.models import AcademicHistory, AcademicProfile

@receiver(signals.post_save, sender=models.StudentRegistration)
def create_registered_semesters(sender, instance, created, **kwargs):
    if created:
        semesters = instance.academic_year.semester_set.all()

        for semester in semesters:
            models.RegisteredSemester.objects.create(
                student=instance.student,
                registration=instance,
                semester=semester,
            )

@receiver(signals.post_save, sender=models.Payment)
def handle_payment_completion(sender, instance, created, **kwargs):
    if instance.status == "completed":
        # Get student registration
        registration = instance.registration
        
        # Create academic history
        academic_history = AcademicHistory.objects.create(
            level=registration.level,
            academic_year=registration.academic_year,
            academic_profile=registration.student.academicprofile
        )
        
        # Update current academy in academic profile
        academic_profile = registration.student.academicprofile
        academic_profile.current_academy = academic_history
        academic_profile.save()