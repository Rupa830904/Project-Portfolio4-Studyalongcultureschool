# Generated by Django 3.2.20 on 2023-08-13 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyalong', '0007_auto_20230813_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Place',
            new_name='place',
        ),
    ]
