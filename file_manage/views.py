from django.shortcuts import render
from file_manage.form import ReportManageForm, ReportSearchForm, ReportDetailForm
from django.http import HttpResponse, FileResponse
from file_manage.models import ReportManage

# Create your views here.

def upload_report(request):
    '''上传报告视图'''
    if request.method == 'POST':
        form = ReportManageForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['file'].name[0:11]
            if ReportManage.objects.filter(file_name=filename).count():
                html = "<html><body>该报告已存在，请联系管理员!</body></html>"
                return HttpResponse(html)
            else:
                report = form.save()
                report.get_file_name()
                report.save()
                html = "<html><body>成功!</body></html>"
                return HttpResponse(html)
    else:
        form = ReportManageForm()
    return render(request, 'file_manage/upload_report.html', {'form': form})

def index_report(request):
    '''
    报告导航视图：
    1、将最近上传的20份报告展示在首页（视情况是否提供翻页功能）
    2、提供搜索栏，可按照年份、月份、编号搜索报告
    3、为首页的20份报告后面提供下载按钮
    '''
    return render(request, 'base.html')

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

def search_report(request):
    '''
    报告搜索视图
    :param request:
    :return:
    '''
    if request.method == "POST":
        form = ReportSearchForm(request.POST)
        if form.is_valid():
            try:
                report = ReportManage.objects.get(file_name=form['report_serial_number'].value())
                context = {'report': report}
                return render(request, 'file_manage/report_detail.html', context)
            except:
                html = "<html><body>没有这份报告，请返回！</body></html>"
                return HttpResponse(html)
    else:
        form = ReportSearchForm()
        reports = ReportManage.objects.order_by('-add_datetime')
        context = {'form': form, 'reports': reports}
    return render(request, 'file_manage/search_report.html', context)

