from django.contrib import admin
from django.urls import path
from . import views

app_name = "oaklims_main"

urlpatterns = [
    path('', views.homepage, name='homepage'),
]