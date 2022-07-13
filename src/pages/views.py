from django.shortcuts import render, redirect
from assets.models import Device
from incidents.models import Incident

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_technician:
            return redirect('technician_workspace')
        devices = Device.objects.filter(client=request.user.client)
        incidents = Incident.objects.filter(client=request.user.client)
        data = {
            'devices': devices,
            'incidents': incidents,
        }
        return render(request, 'pages/home.html', data)
    else:
        return redirect('login')
