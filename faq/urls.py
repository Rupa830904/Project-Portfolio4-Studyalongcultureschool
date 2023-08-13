from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.Postquestion.as_view(), name='faq'),
]