# Generated by Django 5.1.1 on 2024-11-01 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_alter_department_options_alter_faculty_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicyear',
            options={'ordering': ['name'], 'verbose_name': 'year', 'verbose_name_plural': 'years'},
        ),
        migrations.AlterModelOptions(
            name='registrationperiod',
            options={'ordering': ['academic_year'], 'verbose_name': 'period', 'verbose_name_plural': 'periods'},
        ),
    ]
