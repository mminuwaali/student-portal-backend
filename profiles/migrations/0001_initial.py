# Generated by Django 5.1.1 on 2024-11-04 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0005_course_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.academicyear')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.level')),
            ],
            options={
                'verbose_name_plural': 'Academic histories',
                'ordering': ['-academic_year'],
            },
        ),
        migrations.CreateModel(
            name='AcademicProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_academy', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.academichistory')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.department')),
                ('faculty', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='academy.faculty')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='academichistory',
            name='academic_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.academicprofile'),
        ),
        migrations.AlterUniqueTogether(
            name='academichistory',
            unique_together={('academic_year', 'academic_profile')},
        ),
    ]
