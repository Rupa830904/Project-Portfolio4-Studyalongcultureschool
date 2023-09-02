from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'starting_on')
    search_fields = ['title', 'content']
    list_filter = ('title', 'starting_on')
    prepopulated_fields = {'slug': ('title',)}
