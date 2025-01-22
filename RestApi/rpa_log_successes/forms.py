#necessário para criação de itens do front para o back end
from django import forms
from . import models

class RpaLogSuccessForm(forms.ModelForm):
    
    class Meta:
        model = models.RpaLogSuccess
        fields = ['rpa','duration','rpa_log_status','message']

        widgets = {
            'rpa': forms.Select({'class':'form-control'}),
            'duration': forms.TimeInput({'class': 'form-control'}),
            'rpa_log_status':forms.Select({'class':'form-control'}),
            'message': forms.TextInput({'class':'form-control', 'rows': 2})
        }