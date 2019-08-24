
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"oaklims.settings")
import django
django.setup()
from file_manage.models import ReportManage

with open('output.txt', 'w') as f:
    for file in ReportManage.objects.all():
        pk = file.pk
        file_name = file.file_name
        file_dir = file.file.name
        f.write(file_name + ', ' + file_dir + '\n')
