#necessário para criação de itens do front para o back end
from django import forms
from . import models

class RpaLogErrorForm(forms.ModelForm):
    
    class Meta:
        model = models.RpaLogError
        fields = ['rpa','start_time','end_time','rpa_log_status','message']

        widgets = {
            'rpa': forms.Select({'class':'form-control'}),
            'start_time':forms.DateTimeInput({'class':'form-control'}),
            'end_time':forms.DateTimeInput({'class':'form-control'}),
            'rpa_log_status':forms.Select({'class':'form-control'}),
            'message': forms.TextInput({'class':'form-control', 'rows': 2})
        }
        

        labels = {
            'rpa':'Rpa',
            'start_time':'Início do log',
            'end_time':'Fim do log',
            'rpa_log_status':'Status',
            'message':'Mensagem',
        }

