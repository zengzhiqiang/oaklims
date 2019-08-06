from django.forms import ModelForm
from file_manage.models import ReportManage

class ReportManageForm(ModelForm):

    class Meta:
        model = ReportManage
        fields = ['file']
