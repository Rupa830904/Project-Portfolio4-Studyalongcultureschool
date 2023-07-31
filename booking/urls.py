from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingList.as_view(), name='booking'),
    path('booking/', views.CreateBooking.as_view(), name='add_booking'),
]