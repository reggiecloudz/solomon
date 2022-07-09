from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse

from projects.forms.devices import DeviceForm
from projects.forms.issues import IssueForm
from projects.models import Device
from accounts.models import Client
from accounts.decorators import client_required

# Create your views here.
@login_required
@client_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.client = request.user.client
            c.save()
            return redirect('home')
    else:
        form = DeviceForm()
    return render(request, 'devices/form.html', {'form': form})

@login_required
@client_required
def add_issue(request, pk):
    device = Device.objects.get(pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.status = 'Submitted'
            c.device = device
            c.client = request.user.client
            c.save()
            return redirect('home')
    else:
        form = IssueForm()
    return render(request, 'issues/form.html', {'form': form})
