from django import forms

from repairs.models import Repair

class RepairForm(forms.ModelForm):
    subject = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-pill'}))
    explanation = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Repair
        fields = ("subject", "explanation",)

# AcceptOrDeclineForm(instance=repair)
class OfferForm(forms.ModelForm):
    ACCEPT_OR_DECLINE_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
    hourly_rate = forms.DecimalField(max_digits=11, decimal_places=2, min_value=1.00)
    status = forms.ChoiceField(choices=ACCEPT_OR_DECLINE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Repair
        fields = ("hourly_rate", "status",)

class AcceptOrDeclineForm(forms.ModelForm):
    ACCEPT_OR_DECLINE_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
    hourly_rate = forms.DecimalField(max_digits=11, decimal_places=2, min_value=1.00)
    status = forms.ChoiceField(choices=ACCEPT_OR_DECLINE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Repair
        fields = ("hourly_rate", "status",)