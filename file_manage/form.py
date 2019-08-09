from django.forms import ModelForm
from file_manage.models import ReportManage
from django import forms

class ReportManageForm(ModelForm):
    '''
    报告上传表单
    '''
    class Meta:
        model = ReportManage
        fields = ['file']

class ReportSearchForm(forms.Form):
    '''
    搜索报告表单
    '''
    report_serial_number = forms.CharField(label="报告编号", max_length=100)

class ReportDetailForm(forms.Form):
    '''报告详情页，含下载链接'''
    report_name = forms.CharField(label="报告编号", max_length=100)
    download_url = forms.URLField(label="下载链接")