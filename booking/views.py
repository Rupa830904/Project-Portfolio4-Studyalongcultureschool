from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("-booking_date")
    template_name = "booking_list.html"