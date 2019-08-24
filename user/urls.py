from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]