from django import forms
from .models import WorkDescription


class WorkDescriptionForm(forms.ModelForm):
    class Meta:
        model = WorkDescription
        fields = ('status', 'description')
