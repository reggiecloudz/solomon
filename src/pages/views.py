import json
from datetime import datetime, timedelta
from decimal import Decimal
from django.shortcuts import render, redirect

from assets.models import Device, SystemSnapshot
from incidents.models import Job
from incidents.utils import difference_in_mintues, convert_minutes_to_hours, convert_cost

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_technician:
            return redirect('technician_workspace')
        devices = Device.objects.filter(client=request.user.client)
        data = {
            'devices': devices,
        }
        return render(request, 'pages/home.html', data)
    else:
        return redirect('login')

def forplay(request):
    job = Job.objects.get(pk=1)
    template_name = 'pages/forplay.html'
    data = {
        'job': job
    }
    today = datetime.now()
    future_time = today + timedelta(hours=10)
    work_period = {'start': today.__str__(), 'pause': '' }
    
    job.work_periods.insert(0, work_period)
    
    job.work_periods[0]["pause"] = future_time.__str__()
    
    # get the minutes.
    minutes = difference_in_mintues(job.work_periods[0]["start"], job.work_periods[0]["pause"])

    # convert those minutes to hours
    job.hours_worked += convert_minutes_to_hours(minutes)

    # get the cost of the job
    cost = convert_cost(job.support_request.offer.hourly_rate, job.hours_worked)
    
    # job.save()
    # print(job.hours_worked)
    
    return render(request, template_name, data)