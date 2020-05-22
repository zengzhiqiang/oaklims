from django.db import models
from user.models import User
from commissions_of_test.models import Commission
import os
from django.conf import settings


# Create your models here.

def report_path(instance, filename):
    '''根据文件名返回存储路径'''
    return filename[0:4] + '//' + filename[5:7] + '//' + filename


class ReportManage(models.Model):
    '''报告文件管理app'''
    commission = models.OneToOneField(Commission, on_delete=models.CASCADE, verbose_name="送检编号")
    file_name = models.CharField(max_length=32, unique=True)
    file = models.FileField(upload_to=report_path)
    upload_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='upload by+', verbose_name='上传人')
    belong_to = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='belong to+', verbose_name='送检人')
    add_datetime = models.DateTimeField(auto_now_add=True)
    add_date = models.DateField(verbose_name='上传日期', auto_now_add=True)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = "报告列表"
        verbose_name_plural = "报告列表"
        get_latest_by = "add_datetime"

    def get_file_name(self):
        '''获取文件名，存入数据库'''
        self.file_name = self.file.name[0:11]

    def get_download_url(self):
        '''为每一份报告生成下载链接'''
        download_url = self.file_name[0:4] + "//" + self.file_name[5:7] + "//" + self.file_name[8:11] + "//download"
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

    def associate_commission(self):
        self.commission = Commission.objects.get(commission_id=self.file_name)