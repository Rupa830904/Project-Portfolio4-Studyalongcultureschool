from django import forms
#from djrichtextfield.widgets import RichTextWidget
from .models import Booking
from django.contrib.auth.models import User

class SearchBooking(forms.ModelForm):
    """ Form to create a Booking"""
    class Meta:
        model = Booking
        fields = ['booking_name']

        #booking_name = forms.CharField(widget=RichTextWidget())

        labels = {
            'booking_name': 'Full Name'
            
        }

class BookingForm(forms.ModelForm):
    """ Form to create a Booking"""
    class Meta:
        model = Booking
        fields = ['username','personal_number','booking_name','course']

        #booking_name = forms.CharField(widget=RichTextWidget())

        labels = {
            'booking_name': 'Full Name',
            'personal_number' : 'Personal Number',
            'course' : 'choose the course'
        }
