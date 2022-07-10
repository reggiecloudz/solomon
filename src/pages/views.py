from http import client
import re
from django.shortcuts import render, redirect
from repairs.models import Device, Repair

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_technician:
            return redirect('technician_workspace')
        devices = Device.objects.filter(client=request.user.client)
        repairs = Repair.objects.filter(client=request.user.client)
        data = {
            'devices': devices,
            'repairs': repairs,
        }
        return render(request, 'pages/home.html', data)
    else:
        return redirect('login')
