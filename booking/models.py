from django.db import models
from django.contrib.auth.models import User
from studyalong.models import Course
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

# Choice fields
COURSES = (
           ("Indian Classical", "Indian Classical"),
           ("Indian Bollywood", "Indian Bollywood"),
           ("Yoga Dance", "Yoga Dance"), ("Street Dance", "Street Dance"),
           ("Ballet Dance", "Ballet Dance"),
           ("Zumba dance", "Zumba dance"), ("Odissi", "Odissi")
           )


class Booking(models.Model):
    """ Model to book a course """
    booking_name = models.CharField(max_length=25)
    booked_date = models.DateTimeField(default=now, editable=True)
    personal_number = models.CharField(max_length=10)
    course = models.CharField(max_length=30, choices=COURSES)

    class Meta:
        """ Order by booking_date """
        ordering = ['course']

    def __str__(self):
        return str(self.course)


class Bookcourse(models.Model):
    """ Model to book a course """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user")
    booking_name = models.CharField(max_length=25)
    booked_date = models.DateTimeField(default=now, editable=True)
    dob = models.DateField(max_length=8, default=False)
    spring_term = models.BooleanField(default=False)
    autumn_term = models.BooleanField(default=False)
    course = models.CharField(max_length=30, choices=COURSES)

    class Meta:
        """ Order by booking_date """
        ordering = ['booked_date']

    def __str__(self):
        return str(self.course)
