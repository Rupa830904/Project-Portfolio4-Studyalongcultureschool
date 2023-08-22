from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Booking, Bookcourse
from .forms import BookingForm, SearchBooking
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
        messages.success(
            self.request,
            'Course Booked Successfully'
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