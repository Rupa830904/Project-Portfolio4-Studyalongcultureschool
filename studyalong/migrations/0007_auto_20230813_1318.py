# Generated by Django 3.2.20 on 2023-08-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyalong', '0006_rename_featured_image_course_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Place',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
