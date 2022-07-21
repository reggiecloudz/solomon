from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from assets.forms import DeviceForm
from accounts.decorators import client_required

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