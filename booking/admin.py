from django.contrib import admin
from .models import Booking, Bookcourse
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Class to view bookings on admin panel """
    list_display = (
        'course',
        'booked_date',
        'personal_number',
    )
    search_fields = ['booking_name']
    list_filter = ('booking_name','booked_date')

@admin.register(Bookcourse)
class BookcourseAdmin(admin.ModelAdmin):
    """ Class to view bookings on admin panel """
    list_display = (
        'username',
        'course',
        'booked_date',
        'booking_name',
    )
    search_fields = ['booking_name']
    list_filter = ('booking_name','booked_date')
    