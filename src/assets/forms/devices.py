from django import forms

from assets.models import Device

class DeviceForm(forms.ModelForm):
    brand = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-pill'}))
    model = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-pill'}))
    operating_system = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-pill'}))
    about = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Device
        fields = ("brand", "model", "operating_system", "about",)
