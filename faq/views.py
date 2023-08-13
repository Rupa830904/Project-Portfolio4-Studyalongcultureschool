from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import faq
from .forms import QuestionForm
from django.contrib.auth.models import User

# Create your views here.

class Postquestion(CreateView):
    """ Create Booking View """
    model = faq
    form_class = QuestionForm
    template_name = "create_faq.html"
    success_url = '/'

    def form_valid(self, form):
        return super(CreateBooking, self).form_valid(form)