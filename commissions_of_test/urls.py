from django.urls import path
from . import views

app_name = 'commission_of_test'

urlpatterns = [
    path('fill_in/', views.fill_in_commission, name="fill in commission")
]