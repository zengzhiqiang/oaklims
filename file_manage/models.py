from django.db import models
import os
from django.conf import settings


# Create your models here.

def report_path(instance, filename):
    '''根据文件名返回存储路径'''
    return filename[0:4] + '//' + filename[5:7] + '//' + filename


class ReportManage(models.Model):
    '''报告文件管理app'''
    file_name = models.CharField(max_length=32)
    file = models.FileField(upload_to=report_path)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = "报告列表"
        verbose_name_plural = "报告列表"

    def get_file_name(self):
        '''获取文件名，存入数据库'''
        self.file_name = self.file.name[8:19]

    def get_download_url(self):
        '''为每一份报告生成下载链接'''
        download_url = self.file_name[0:4] + "\\" + self.file_name[5:7] + "\\" + self.file_name[8:11] + "\\download"
        return download_url

    def get_report_year(self):
        year = self.file_name[0:4]
        return year

    def get_report_month(self):
        month = self.file_name[5:7]
        return month

    def get_report_number(self):
        number = self.file_name[8:11]
        return number
