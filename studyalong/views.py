from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Course

# Create your views here.

class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.order_by("-starting_on")
    template_name = "index.html"

class CourseDetail(DetailView):
    model = Course
    queryset = Course.objects.order_by("-starting_on")
    template_name = "course_detail.html"
