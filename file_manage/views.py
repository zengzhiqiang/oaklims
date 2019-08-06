from django.shortcuts import render
from file_manage.form import ReportManageForm
from file_manage.models import ReportManage
from django.http import HttpResponse

# Create your views here.

def upload_report(request):
    '''上传报告视图'''
    if request.method == 'POST':
        print(request.POST)
        print("-------------")
        print(request.FILES)
        print("-------")
        form = ReportManageForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            report = form.save()
            report.get_file_name()
            report.save()
            html = "<html><body>成功!</body></html>"
            return HttpResponse(html)
    else:
        form = ReportManageForm()
        print(form)
    return render(request, 'file_manage/upload_report.html', {'form': form})
