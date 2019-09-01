from django.shortcuts import render
from .form import CommissionForm


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