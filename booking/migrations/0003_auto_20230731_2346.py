# Generated by Django 3.2.20 on 2023-07-31 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['course']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
    ]
