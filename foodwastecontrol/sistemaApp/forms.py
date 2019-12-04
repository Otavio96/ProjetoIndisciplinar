from django.forms import ModelForm
from .models import Empresa
        
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_fantasia','cnpj','quantidade_funcionarios', 'estado', 'cidade']

    