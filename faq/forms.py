from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
#from djrichtextfield.widgets import RichTextWidget
from .models import faq
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = faq
        fields = ['name','email','question']
        name = forms.CharField()
        email = forms.CharField()
        question = forms.CharField()

        labels = {
            'name': 'name',
            'email': 'Email',
            'question' : 'question',
        }

class AnswerForm(forms.ModelForm):
    """ Form to answer a question"""
    class Meta:
        model = faq
        fields = ['answer']
        answer = forms.CharField()

        labels = {
            'answer' : 'answer',
        }