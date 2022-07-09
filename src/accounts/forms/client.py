from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User, Client


class ClientSignUpForm(UserCreationForm):
    email = forms.CharField(min_length=1, max_length=60, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    name = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(min_length=1, max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta(UserCreationForm):
        model = User
        fields = ('name', 'email')

    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        Client.objects.create(identity=user)
        return user
