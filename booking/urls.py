from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.Booking.as_view(), name='booking'),
    path('booking/', views.CreateBooking.as_view(), name='add_booking'),
    path('view-booking/', views.BookingList.as_view(), name='view_booking'),
    path(
        'delete/<slug:pk>/', views.DeleteBooking.as_view(),
        name='delete_booking'
        ),
    path('edit/<slug:pk>/', views.EditBooking.as_view(), name='edit_booking'),
    path(
        'search-booking/', views.SearchBooking.as_view(),
        name='search_booking'
        ),
]
