from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User, Technician


class TechnicianSignUpForm(UserCreationForm):
    email = forms.CharField(min_length=1, max_length=60, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    password1 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email',)

    def save(self):
        user = super().save(commit=False)
        user.is_technician = True
        user.save()
        Technician.objects.create(identity=user)
        return user