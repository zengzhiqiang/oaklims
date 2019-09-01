from django.urls import path
from . import views

app_name = 'commission_of_test'

urlpatterns = [
    path('fill_in/', views.fill_in_commission, name="fill in commission"),
    path('search/$', views.search_commission, name="search commission"),
    path('<int:year>/<int:month>/<int:serial_number>/detail/', views.commission_detail, name="commission detail"),
    path('<str:year>/<str:month>/<str:number>/upload_report/', views.upload_report, name="upload report"),
]