# Generated by Django 3.2.20 on 2023-08-01 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20230731_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_datedate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
