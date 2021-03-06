from django.urls import path
from . import views

app_name = 'commission_of_test'

urlpatterns = [
    path('fill_in/', views.fill_in_commission, name="fill in commission"),
    path('<int:pk>/detail/', views.commission_detail, name="commission detail"),
    path('<int:pk>/upload_report/', views.upload_report, name="upload report"),
    path('index/', views.index, name="index"),
]