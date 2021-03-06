
from django.urls import path
from . import views

app_name = "file_manage"

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('index', views.index_report, name="index report"),
    path('upload', views.upload_report, name="upload report"),
    path('<int:pk>/download/', views.download_report, name="download report"),
    path('search/', views.search_report, name="search report")
]