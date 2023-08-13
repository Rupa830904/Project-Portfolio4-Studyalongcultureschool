from django.db import models

# Create your models here.

class faq(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    question = models.TextField()
    answer = models.TextField(default = "We will get back to you soon")

    class Meta:
        ordering = ["-question"]

    def __str__(self):
        return self.name