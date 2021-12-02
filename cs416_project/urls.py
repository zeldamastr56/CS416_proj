from django.contrib import admin
from django.urls import path, include
import restaurant.views

urlpatterns = [
    path('', include('restaurant.urls')),
]
