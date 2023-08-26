from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('details/<slug:slug>', views.CourseDetail.as_view(), name='course_detail'),
    path('course/', views.AddCourse.as_view(), name='add_course'),
    path('edit/<slug:slug>', views.EditCourse.as_view(), name='edit_course'),
    path('check-course/<slug:slug>', views.Checkcourse.as_view(), name='check_course'),
]