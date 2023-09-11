from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Course
from booking.models import Bookcourse
from .forms import CourseForm, AddcourseForm

# Create your views here.


class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.order_by("starting_on")
    template_name = "index.html"


class CourseDetail(DetailView):
    model = Course
    queryset = Course.objects.order_by("starting_on")
    template_name = "course_detail.html"


class EditCourse(LoginRequiredMixin, UpdateView):
    """ Edit a booking """
    model = Course
    template_name = "edit_course.html"
    form_class = CourseForm
    success_url = '/'


class AddCourse(LoginRequiredMixin, CreateView):
    """ Edit a booking """
    model = Course
    template_name = "add_course.html"
    form_class = AddcourseForm
    success_url = '/'


class Checkcourse(LoginRequiredMixin, ListView):
    """Searcg a booking view """
    model = Bookcourse
    template_name = "check_course.html"
    context_object_name = 'place_left'

    def get_queryset(self):
        item = self.request.GET.get('course')
        total_booking = Bookcourse.objects.filter(course=item).count()
        place_left = 10 - total_booking
        return place_left
