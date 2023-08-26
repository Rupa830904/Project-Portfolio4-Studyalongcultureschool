from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from cloudinary.models import CloudinaryField
#from djrichtextfield.widgets import RichTextWidget
from .models import Course
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    """ Form to edit a course"""
    class Meta:
        model = Course
        fields = ['content','teacher','place','starting_on']
        content = forms.CharField()
        place = forms.CharField()
        teacher = forms.CharField()
    
        labels = {
            'content': 'content',
            'teacher': 'teacher',
            'place' : 'place',
            'starting_on' : 'starting_on',
        }

        widgets = {
        'starting_on': DateInput(attrs={'type': 'date'})
        }

class AddcourseForm(forms.ModelForm):
    """ Form to add a course"""
    class Meta:
        model = Course
        fields = ['title','course_image','content','teacher','place','starting_on']
        title = forms.CharField()
        content = forms.CharField()
        place = forms.CharField()
        teacher = forms.CharField()
    
        labels = {
            'content': 'content',
            'teacher': 'teacher',
            'place' : 'place',
            'starting_on' : 'starting_on',
        }

        widgets = {
        'starting_on': DateInput(attrs={'type': 'date'})
        }