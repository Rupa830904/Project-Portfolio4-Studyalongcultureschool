from django.contrib import admin
from .models import Course, Interest
#from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'starting_on')
    search_fields = ['title', 'content']
    list_filter = ('title','starting_on')
    prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)

@admin.register(Interest)

class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'course','created_on', 'acknowledged')
    list_filter = ('acknowledged', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['acknowledge_interests']

    def acknowledge_interests(self, request, queryset):
        queryset.update(approved=True)