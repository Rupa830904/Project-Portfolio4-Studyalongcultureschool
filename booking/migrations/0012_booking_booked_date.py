# Generated by Django 3.2.20 on 2023-08-11 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_booking_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
