from django.forms import ModelForm
from file_manage.models import ReportManage
from django import forms

class ReportManageForm(ModelForm):
    '''
    报告上传表单
    '''
    class Meta:
        model = ReportManage
        fields = ['file', 'upload_by', 'belong_to']

class ReportSearchForm(forms.Form):
    '''
    搜索报告表单
    '''
    report_serial_number = forms.CharField(label="报告编号", max_length=100)
