from django.urls import path
from . import views

app_name = 'booking_manager'

urlpatterns = [
    path('', views.main, name='booking_manager'),
    path('services/', views.services, name='services'),
    path('specialist/', views.specialists, name='specialist'),
    path('booking/', views.booking, name='booking'),
    path('new_booking/', views.new_booking, name='new_booking'),
]