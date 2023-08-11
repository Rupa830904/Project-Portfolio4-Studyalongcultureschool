from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm, SearchBooking
from django.contrib.auth.models import User

# Create your views here.

class BookingList(generic.ListView):
    """ Read Booking view """
    model = Booking
    queryset = Booking.objects.order_by("-username")
    template_name = "booking_detail.html"

class CreateBooking(LoginRequiredMixin, CreateView):
    """ Create Booking View """
    model = Booking
    form_class = BookingForm
    template_name = "create_booking.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBooking, self).form_valid(form)

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a booking """
    model = Booking
    template_name = "booking_confirm_delete.html"
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().username

class Booking(generic.ListView):
    """Booking view """
    model = Booking
    template_name = "booking.html"