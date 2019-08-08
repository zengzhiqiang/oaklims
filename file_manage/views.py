from django.shortcuts import render
from file_manage.form import ReportManageForm
from file_manage.models import ReportManage
from django.http import HttpResponse, FileResponse
from file_manage.models import ReportManage

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

def index_report(request):
    '''
    报告导航视图：
    1、将最近上传的20份报告展示在首页（视情况是否提供翻页功能）
    2、提供搜索栏，可按照年份、月份、编号搜索报告
    3、为首页的20份报告后面提供下载按钮
    '''
    pass

def download_report(request, year, month, serial_number):
    '''
    报告下载视图，提供下载报告的链接
    :param request:
    :param year: 报告年份
    :param month: 报告月份
    :param serial_number: 报告编号
    :return:
    '''
    report_name = str(year) + "-" + str(month).zfill(2) + "-" + str(serial_number).zfill(3)
    report = ReportManage.objects.get(file_name=report_name)
    f = open(report.file.path, 'rb')
    response = FileResponse(f)
    response['Content-Type'] = 'application/pdf;charset=utf-8'
    response['Content-Disposition'] = 'attachment;filename=' + report.file_name + '.pdf'
    return response
