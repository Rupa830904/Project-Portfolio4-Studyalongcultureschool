from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('details/<slug:slug>', views.CourseDetail.as_view(), name='course_detail'),
    path('edit/<slug:slug>', views.EditBooking.as_view(), name='edit_course'),
]