from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView

from accounts.decorators import client_required, technician_required
from accounts.forms.client import ClientSignUpForm
from accounts.forms.technician import TechnicianSignUpForm
from accounts.models import Client, User, Technician
# from incidents.models import Incident

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class TechnicianSignUpView(CreateView):
    model = User
    form_class = TechnicianSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@technician_required
def technician_workspace(request):
    # incidents = Incident.objects.all()
    data = {
        # 'incidents': incidents,
    }
    return render(request, 'technicians/workspace.html', data)