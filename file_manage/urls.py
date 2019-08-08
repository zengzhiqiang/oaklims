
from django.urls import path
from . import views

app_name = "file_manage"

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('index', views.index_report, name="index report"),
    path('upload', views.upload_report, name="upload report"),
    path('<int:year>/<int:month>/<int:serial_number>/download/', views.download_report, name="download report"),
]