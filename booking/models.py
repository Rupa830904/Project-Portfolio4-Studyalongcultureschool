from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Choice fields
COURSES = ((1, "Indian Classical"), (2, "	Indian Bollywood"), (3, "Yoga Dance"), (4, "Street Dance"), (5, "Ballet Dance"), (6, "Zumba dance"))


class Booking(models.Model):
    """ Model to book a course """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user")
    booking_name = models.CharField(max_length=25)
    booking_date = models.DateField()
    course = models.IntegerField(choices=COURSES)

    class Meta:
        """ Order by booking_date """
        ordering = ['booking_date']

    def __str__(self):
        return str(self.course)