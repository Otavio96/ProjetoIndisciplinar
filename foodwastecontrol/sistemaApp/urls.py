from django.urls import path
from .views import cadastrar_empresas
from .views import visualizar_empresas

urlpatterns = [
    path('cadastrar', cadastrar_empresas, name="cadastro_empresas"),
    path('visualizar', visualizar_empresas, name="visualizar_empresa"),
]