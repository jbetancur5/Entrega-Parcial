from django.urls import path
from . import views

app_name = 'vuelos'

urlpatterns = [
    path('', views.register_flight, name='register_flight'),
    path('list/', views.list_flights, name='list_flights'),
    path('stats/', views.flight_stats, name='flight_stats'),
]