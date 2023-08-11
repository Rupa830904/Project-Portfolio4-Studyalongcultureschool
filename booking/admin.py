from django.contrib import admin
from .models import Booking
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Class to view bookings on admin panel """
    list_display = (
        'username',
        'course',
        'booked_date',
    )
    search_fields = ['booking_name']
    list_filter = ('username','booking_name','booked_date')
    