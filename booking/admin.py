from django.contrib import admin
from .models import Booking
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Class to view bookings on admin panel """
    list_display = (
        'username',
        'booking_date',
        'booking_name',
        'course'
    )
    search_fields = ['booking_name', 'booking_date']
    list_filter = ('booking_date', 'course')
    