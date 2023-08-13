from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import faq
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.models import User

# Create your views here.


class Faqlist(ListView):
    """ Create Booking View """
    model = faq
    template_name = "faq.html"
    success_url = '/'

class Postquestion(CreateView):
    """ Create Booking View """
    model = faq
    form_class = QuestionForm
    template_name = "create_faq.html"
    success_url = '/'

class Ansquestion(UpdateView):
    """ Create Booking View """
    model = faq
    form_class = AnswerForm
    template_name = "answer_faq.html"
    success_url = '/'