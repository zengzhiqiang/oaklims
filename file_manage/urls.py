
from django.urls import path
from . import views

app_name = "file_manage"

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('upload', views.upload_report, name="upload report")
]