from django.contrib import admin
from .models import faq
from django.contrib.auth.models import User
# Register your models here.

@admin.register(faq)
class faqAdmin(admin.ModelAdmin):
    """ Class to view bookings on admin panel """
    list_display = (
        'name',
        'question',
        'answer',
    )
    search_fields = ['name']
    list_filter = ('name','email')

# Register your models here.
