from django import forms
from .models import Coroa, Forma, Bloco


class CoroaTeste(forms.ModelForm):
    class Meta:
        model = Coroa
        fields = ['código', 'número', 'colo_superior', 'colo_inferior', 'furo_anel', 'folga_anel', 'encaixe_co_bl', 'externo', 'situacao_final', 'data', 'lote', 'colaborador'
]
        
class FormaTeste(forms.ModelForm):
    class Meta:
        model = Forma
        fields = ['código', 'número', 'colo', 'rodape', 'flexa', 'furo_de_escape', 'encaixe_ffo', 'externo', 'situacao_final', 'data', 'lote', 'colaborador'
]
        
class BlocoTeste(forms.ModelForm):
    class Meta:
        model = Bloco
        fields = ['código', 'número', 'colo', 'rodape', 'flexa', 'furo_de_escape', 'encaixe_ffo', 'externo', 'situacao_final', 'data', 'lote', 'colaborador'
]