import json
from datetime import datetime
from django.shortcuts import render, redirect
from assets.models import Device
from incidents.models import Incident
from documentation.models import SystemDescription

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

def forplay(request):
    description = SystemDescription.objects.get(pk=1)
    template_name = 'pages/forplay.html'
    data = {
        'description': description
    }
    # new_item = {'key5': 'value5', 'timestamp': datetime.now().__str__() }
    # description.display_type.insert(0, new_item)
    # description.save()
    return render(request, template_name, data)