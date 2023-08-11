from django import forms
from django.forms.widgets import DateInput
#from djrichtextfield.widgets import RichTextWidget
from .models import Booking, Bookcourse
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
        model = Bookcourse
        fields = ['username','booking_name','course','dob']
        booking_name = forms.CharField()
        spring_term = forms.CheckboxInput()
        autumn_term = forms.CheckboxInput()
        #days = widgets = { 'days': forms.CheckboxSelectMultiple }
        #booking_name = forms.CharField(widget=RichTextWidget())

        labels = {
            'username': 'Username',
            'booking_name': 'Full Name',
            'dob' : 'Date Of Birth',
            'course' : 'choose the course',
        }

        widgets = {
        'dob': DateInput(attrs={'type': 'date'})
        }