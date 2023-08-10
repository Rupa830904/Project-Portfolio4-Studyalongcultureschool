from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.Booking.as_view(), name='booking'),
    path('booking/', views.CreateBooking.as_view(), name='add_booking'),
    path('view-booking/', views.BookingList.as_view(), name='view_booking'),
]