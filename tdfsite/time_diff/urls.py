from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_time_difference, name='time_difference'),
]
