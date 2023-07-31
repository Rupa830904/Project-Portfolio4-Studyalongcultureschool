from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm

# Create your views here.

class BookingList(generic.ListView):
    """ Read Booking view """
    model = Booking
    queryset = Booking.objects.order_by("-booking_date")
    template_name = "booking_list.html"

class CreateBooking(LoginRequiredMixin, CreateView):
    """ Create Booking View """
    model = Booking
    form_class = BookingForm
    template_name = "create_booking.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBooking, self).form_valid(form)