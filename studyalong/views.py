from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.

class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.order_by("-starting_on")
    template_name = "index.html"
