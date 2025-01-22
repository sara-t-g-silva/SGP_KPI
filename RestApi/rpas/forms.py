#necessário para criação de itens do front para o back end
from django import forms
from rpas.models import Rpa

class RpaForm(forms.ModelForm):
    
    class Meta:
        model = Rpa
        fields = ['name','description','rpa_status','error_count']

        widgets = {
            'name': forms.TextInput({'class':'form-control'}),
            'description': forms.Textarea({'class': 'form-control', 'rows': 3}),
            'rpa_status':forms.TextInput({'class':'form-control'}),
            'error_count':forms.NumberInput({'class':'form-control'}),

        }

        labels = {
            'name':'Nome',
            'description':'Descrição',
            'rpa_status':'Status',
            'error_count': 'Quantidade de erros'
        }
