from django.urls import path
from feedback import views

urlpatterns = [
    path('contact/', views.contact)
]