from http import client
import re
from django.shortcuts import render, redirect
from projects.models import Device, Issue

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        devices = Device.objects.filter(client=request.user.client)
        issues = Issue.objects.filter(client=request.user.client)
        data = {
            'devices': devices,
            'issues': issues,
        }
        return render(request, 'pages/home.html', data)
    else:
        return redirect('login')
