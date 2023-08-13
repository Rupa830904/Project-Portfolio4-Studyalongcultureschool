from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.Faqlist.as_view(), name='faq'),
    path('post-faq/', views.Postquestion.as_view(), name='ask_faq'),
]