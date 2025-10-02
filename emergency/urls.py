from django.urls import path
from . import views

app_name = "emergency"

urlpatterns = [
    path('', views.emergency, name='emergency'),   # /emergency/
]