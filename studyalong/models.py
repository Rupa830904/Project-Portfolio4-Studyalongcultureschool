from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    course_image = CloudinaryField('image', default='placeholder')
    #excerpt = models.TextField(blank=True)
    #updated_on = models.DateTimeField(auto_now=True,)
    content = models.TextField()
    starting_on = models.DateField(null=True)
    #status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-starting_on"]

    def __str__(self):
        return self.title

class Interest(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                             related_name="interests")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(null=True)
    acknowledged = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"