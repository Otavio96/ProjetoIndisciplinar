from django.forms import ModelForm
from .models import Person, Usuario, Empresa, Refeicao, Alimento

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio']
        
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'numero_cracha', 'senha']
        
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_fantasia', 'cnpj', 'quantidade_funcionarios', 'estado', 'cidade']
        
class RefeicaoForm(ModelForm):
    class Meta:
        model = Refeicao
        fields = ['quantidade_alimento', 'data_refeicao', 'alimento', 'empresa','usuario']

class AlimentoForm(ModelForm):
    class Meta:
        model = Alimento
        fields = ['nome_alimento', 'valor_alimento']
    