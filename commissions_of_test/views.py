from django.shortcuts import render
from .form import CommissionForm
from commissions_of_test.models import Commission
from file_manage.form import ReportManageForm

# Create your views here.

def fill_in_commission(request):
    '''填写送检单视图'''
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': '保存成功'}
            return render(request, 'commission_of_test/message.html', context)
    else:
        form = CommissionForm()
    return render(request, 'commission_of_test/fill_in_commission.html', {'form': form})

def commission_detail(request, year, month, serial_number):
    '''送检单详情视图'''
    commission_id = str(year) + "-" + str(month).zfill(2) + "-" + str(serial_number).zfill(3)
    commission = Commission.objects.get(commission_id=commission_id)
    context = {'commission': commission}
    return render(request, 'commission_of_test/commission_detail.html', context)

def upload_report(request, year, month, number):
    '''将报告上传到指定送检单'''
    if request.method == "POST":
        form = ReportManageForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.get_file_name()
            print(report.file_name)
            commission_id = year + '-' + month + '-' + number
            print(commission_id)
            if report.file_name == commission_id:
                report.associate_commission()
                report.save()
                commission = Commission.objects.get(commission_id=commission_id)
                commission.test_status = 2
                commission.save()
                message = "上传成功"
                return render(request, 'commission_of_test/message.html', {'message': message})
            else:
                message = "您上传的报告编号与送检单编号不匹配，请核对后上传！"
                return render(request, 'commission_of_test/message.html', {'message': message})
    else:
        form = ReportManageForm()
        message = "请上传编号为" + year + '-' + month + '-' + number + "的报告！"
        context = {
            'form': form,
            'message': message,
            'year': year,
            'month': month,
            'number': number,
        }
        return render(request, 'commission_of_test/upload_report.html', context)

def index(request):
    commissions = Commission.objects.all()
    context = {
        'commissions': commissions
    }
    return render(request, "commission_of_test/index.html", context)