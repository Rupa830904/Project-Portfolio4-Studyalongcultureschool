# Generated by Django 3.2.20 on 2023-08-02 10:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0007_alter_booking_personal_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
