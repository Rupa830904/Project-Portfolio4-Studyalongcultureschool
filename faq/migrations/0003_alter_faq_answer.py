# Generated by Django 3.2.20 on 2023-08-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_faq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(default=False, null=True),
        ),
    ]