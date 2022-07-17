from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from assets.models import Device
from accounts.decorators import client_required, technician_required

'''
@login_required
@client_required
def report_incident(request, pk):
    device = Device.objects.get(pk=pk)
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.status = 'Submitted'
            c.device = device
            c.client = request.user.client
            c.save()
            return redirect('home')
    else:
        form = IncidentForm()
    return render(request, 'incidents/form.html', {'form': form})

@login_required
@technician_required
def review_incident(request, pk):
    incident = Incident.objects.get(pk=pk)
    if (incident.status == 'Submitted'):
        incident.status = 'Review'
        incident.save()
    if request.method == 'POST':
        form = AcceptOrDeclineForm(request.POST, instance=incident)
        if form.is_valid():
            c = form.save(commit=False)
            c.technician = request.user.technician
            c.save()
            return redirect('technician_workspace')
    form = AcceptOrDeclineForm(instance=incident)
    data = {
        'incident': incident,
        'form': form,
    }
    return render(request, 'incidents/review.html', data)
'''
