from django.contrib import admin
from django.urls import path

from mapAdminApp.views import HomeView,GeolocationView 

urlpatterns = [
    path("", HomeView.as_view(), name='my_home_view'), 
    path('geolocation/', GeolocationView.as_view(), name='geolocation'),
]