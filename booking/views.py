from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages
from .models import Booking, Bookcourse
from .forms import BookingForm, SearchForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class BookingList(generic.ListView):
    """ Read Booking view """
    model = Bookcourse
    queryset = Bookcourse.objects.order_by("-course")
    template_name = "booking_detail.html"

class CreateBooking(LoginRequiredMixin, CreateView):
    """ Create Booking View """
    model = Bookcourse
    form_class = BookingForm
    template_name = "create_booking.html"
    success_url = '/mybooking/'

    def form_valid(self, form):
        form.instance.username = self.request.user
        name = form.cleaned_data['booking_name']
        course = form.cleaned_data['course']
        dob = form.cleaned_data['dob']
        check_booking = Bookcourse.objects.filter(booking_name = name, course = course)
        check_total = Bookcourse.objects.filter(course = course).count()
        today = datetime.today()
        age = int(today.year) - int(dob.year) 
        if check_booking.exists():
            messages.success(
            self.request,
            f'Booking already exists for {name} in {course} . Please go to MANAGE MY BOOKING'
            )
            return super(CreateBooking, self).form_invalid(form)
        if check_total == 10:
            messages.success(
            self.request,
            f'The {course} course is full'
            )
            return super(CreateBooking, self).form_invalid(form)
        if age < 5:
            messages.success(
            self.request,
            f'Minimum age to join a course is 5.{name} is welcome later'
            )
            return super(CreateBooking, self).form_invalid(form)
        else :
          messages.success(
            self.request,
            'Course Booked Successfully.'
          )
        return super(CreateBooking, self).form_valid(form)

class EditBooking(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit a booking """
    model = Bookcourse
    template_name = "edit_booking.html"
    form_class = BookingForm
    success_url = '/mybooking/'
    success_message = "Booking updated Successfully"

    def test_func(self):
        return self.request.user == self.get_object().username

class DeleteBooking(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    """ Delete a booking """
    model = Bookcourse
    template_name = "booking_confirm_delete.html"
    success_url = '/mybooking/'
    success_message = "Booking deleted Successfully"

    def test_func(self):
        return self.request.user == self.get_object().username



class Booking(generic.ListView):
    """Booking view """
    model = Bookcourse
    template_name = "booking.html"

class SearchBooking(ListView):
    """Searcg a booking view """
    model = Bookcourse
    template_name = "search_booking.html"
    context_object_name = 'bookinglist'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Bookcourse.objects.filter(booking_name__icontains=query).order_by("-booked_date")
        return  queryset

