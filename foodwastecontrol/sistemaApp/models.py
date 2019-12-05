from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=30)
    quantidade_funcionarios = models.IntegerField()
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome_fantasia

class Alimento(models.Model):
    nome_alimento = models.CharField(max_length=30)
    valor_alimento = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.nome_alimento
    
class Refeicao(models.Model):
    quantidade_alimento = models.IntegerField()
    data_refeicao = models.DateField(auto_now=False, auto_now_add=False)
    alimento = models.ForeignKey(Alimento, null=True, blank=True, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.PROTECT)
    
class Desperdicio(models.Model):
    kg_desperdicio_total = models.DecimalField(max_digits=5, decimal_places=2)
    id_refeicao = models.ForeignKey(Refeicao, null=True, blank=True, on_delete=models.PROTECT)
    