from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    course_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    teacher = models.CharField(max_length=100, default=False)
    place = models.CharField(max_length=100, default=False)
    starting_on = models.DateField(null=True)

    class Meta:
        ordering = ["-starting_on"]

    def __str__(self):
        return self.title
