from django.forms import ModelForm
from .models import Person, Empresa, Refeicao, Alimento

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio']
        
        
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_fantasia', 'cnpj', 'quantidade_funcionarios', 'estado', 'cidade']
        
class RefeicaoForm(ModelForm):
    class Meta:
        model = Refeicao
        fields = ['quantidade_alimento', 'data_refeicao', 'alimento', 'empresa']

class AlimentoForm(ModelForm):
    class Meta:
        model = Alimento
        fields = ['nome_alimento', 'valor_alimento']
    