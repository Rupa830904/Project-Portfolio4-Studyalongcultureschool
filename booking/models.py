from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Choice fields
COURSES = (("Indian Classical", "Indian Classical"), ("Indian Bollywood","Indian Bollywood"), ("Yoga Dance","Yoga Dance"), ("Street Dance","Street Dance"), ("Ballet Dance","Ballet Dance"), ("Zumba dance","Zumba dance"))


class Booking(models.Model):
    """ Model to book a course """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user")
    booking_name = models.CharField(max_length=25)
    booking_date = models.DateField()
    course = models.CharField(max_length=30, choices=COURSES)

    class Meta:
        """ Order by booking_date """
        ordering = ['booking_date']

    def __str__(self):
        return str(self.course)