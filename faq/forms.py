from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
#from djrichtextfield.widgets import RichTextWidget
from .models import faq
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    """ Form to create a Booking"""
    class Meta:
        model = faq
        fields = ['name','email','question']
        name = forms.CharField()
        email = forms.CharField()
        question = forms.CharField()
        #days = widgets = { 'days': forms.CheckboxSelectMultiple }
        #booking_name = forms.CharField(widget=RichTextWidget())

        labels = {
            'name': 'name',
            'email': 'Email',
            'question' : 'question',
        }