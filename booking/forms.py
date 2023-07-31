from django import forms
#from djrichtextfield.widgets import RichTextWidget
from .models import Booking
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    """ Form to create a Booking"""
    class Meta:
        model = Booking
        fields = ['username','booking_name','booking_date','course']

        #booking_name = forms.CharField(widget=RichTextWidget())

        labels = {
            'booking_name': 'First Name & Last name',
            'booking_date' : 'Date of Booking',
            'course' : 'Select the course'
        }
