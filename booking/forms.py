from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Booking, Bookcourse
from django.contrib.auth.models import User


class SearchForm(forms.ModelForm):
    """ Form to search a Booking"""
    class Meta:
        model = Bookcourse
        fields = ['booking_name']
        labels = {
            'booking_name': 'Full Name'
        }


class BookingForm(forms.ModelForm):
    """ Form to create a Booking"""
    class Meta:
        model = Bookcourse
        fields = ['booking_name', 'course', 'dob', 'spring_term', 'autumn_term']
        booking_name = forms.CharField()
        spring_term = forms.CheckboxInput()
        autumn_term = forms.CheckboxInput()

        labels = {
            'username': 'Username',
            'booking_name': 'Full Name',
            'dob': 'Date Of Birth',
            'course': 'choose the course',
        }

        widgets = {'dob': DateInput(attrs={'type': 'date'})}
