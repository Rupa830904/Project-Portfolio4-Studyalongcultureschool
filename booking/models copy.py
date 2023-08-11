from django.db import models
from django.contrib.auth.models import User
from studyalong.models import Course
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

#Choice fields
COURSES = (("Indian Classical", "Indian Classical"), ("Indian Bollywood","Indian Bollywood"), ("Yoga Dance","Yoga Dance"), ("Street Dance","Street Dance"), ("Ballet Dance","Ballet Dance"), ("Zumba dance","Zumba dance"))

class Booking(models.Model):
    """ Model to book a course """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user")
    booking_name = models.CharField(max_length=25)
    booked_date = models.DateTimeField(default=now, editable=True)
    dob = models.DateField(max_length=8,default=False)
    personal_number = models.CharField(max_length=25)
    spring_term = models.BooleanField(default=False)
    autumn_term = models.BooleanField(default=False)
    days = models.CharField(max_length=10, choices=DAYS_OF_WEEK, default=False)
    course = models.CharField(max_length=30, choices=COURSES)


    class Meta:
        """ Order by booking_date """
        ordering = ['course']

    def __str__(self):
        return str(self.course)