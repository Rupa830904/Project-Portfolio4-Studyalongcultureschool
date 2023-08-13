from . import views
from django.urls import path, reverse

urlpatterns = [
    path('', views.Faqlist.as_view(), name='faq'),
    path('post-faq/', views.Postquestion.as_view(), name='ask_faq'),
    path('ans-faq/<slug:pk>/', views.Ansquestion.as_view(), name='ans_faq'),
]