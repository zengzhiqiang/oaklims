from django.shortcuts import render
from file_manage.form import ReportManageForm, ReportSearchForm
from django.http import FileResponse
from file_manage.models import ReportManage
from commissions_of_test.models import Commission


# Create your views here.

def upload_report(request):
    '''上传报告视图'''
    if request.method == 'POST':
        form = ReportManageForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.cleaned_data['file'].name[0:11]
            if ReportManage.objects.filter(file_name=filename).count():
                context = {'message': '报告已存在，请联系管理员'}
                return render(request, 'file_manage/message.html', context)
            else:
                report = form.save(commit=False)
                report.get_file_name()
                report.associate_commission()
                commission = Commission.objects.get(commission_id=report.file_name)
                commission.test_status = 2
                commission.save()
                report.save()
                context = {'message': '上传成功！'}
                return render(request, 'file_manage/message.html', context)
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

def download_report(request, pk):
    '''
    报告下载视图，提供下载报告的链接
    :param request:
    :param year: 报告年份
    :param month: 报告月份
    :param serial_number: 报告编号
    :return:
    '''

    report = ReportManage.objects.get(commission_id=pk)
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
                context = {'message': '没有这份报告'}
                return render(request, 'file_manage/message.html', context)
    else:
        form = ReportSearchForm()
        reports = ReportManage.objects.order_by('-add_datetime')
        commissions = Commission.objects.all()
        context = {'form': form, 'reports': reports, 'commissions': commissions}
    return render(request, 'file_manage/search_report.html', context)

def change_report(request):
    '''修改已上传的报告'''
    pass