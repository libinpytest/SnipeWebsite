from django import forms
from .models import Service

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'photo']
