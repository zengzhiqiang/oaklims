from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/user/login')
def homepage(request):
    return render(request, 'oaklims_main/homepage.html')

def noyet(request):
    return  render(request, 'oaklims_main/noyet.html')
