from django import forms
from .models import Infos

class InfosForm(forms.ModelForm):
    
    class Meta:
        model = Infos
        fields = ['title', 'summary', 'running_time']