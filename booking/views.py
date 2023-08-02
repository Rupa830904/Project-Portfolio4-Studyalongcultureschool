from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm, SearchBooking
from django.contrib.auth.models import User

# Create your views here.

class BookingList(generic.ListView):
    """ Read Booking view """
    model = Booking
    queryset = Booking.objects.order_by("-course")
    template_name = "booking_list.html"

class CreateBooking(LoginRequiredMixin, CreateView):
    """ Create Booking View """
    model = Booking
    form_class = BookingForm
    template_name = "create_booking.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBooking, self).form_valid(form)

class SearchBooking(LoginRequiredMixin, CreateView):
    """ Create Search Booking View """
    model = Booking
    form_class = SearchBooking
    template_name = "search_booking.html"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SearchBooking, self).form_valid(form)

class BookingListEdit(generic.ListView):
    """ Read Booking view """
    model = Booking
    queryset = Booking.objects.order_by("-course")
    template_name = "edit_booking.html"