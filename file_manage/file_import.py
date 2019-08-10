
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oaklims.settings")
import django
django.setup()
from file_manage.models import ReportManage

with open(r'F:\曾志强\实验报告\已完成\报告数据.txt', 'r') as f:
    '''报告数据导入'''
    for line in f.readlines():
        report_date = ReportManage()
        print(line.split(', '))
        report_date.file_name = line.split(', ')[0]
        report_date.file = line.split(', ')[1][0:23]
        print(report_date.file_name)
        print(report_date.file)
        report_date.save()
