from re import I
from django import forms

from projects.models import Issue

class IssueForm(forms.ModelForm):
    subject = forms.CharField(min_length=1, max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-pill'}))
    explanation = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Issue
        fields = ("subject", "explanation",)
