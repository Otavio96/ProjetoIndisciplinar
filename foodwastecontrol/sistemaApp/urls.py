from django.urls import path
from .views import usuarios_list
from .views import usuarios_new

from .views import empresas_list
from .views import empresas_new
from .views import empresas_update
from .views import empresas_delete

from .views import refeicaos_list
from .views import refeicaos_new
from .views import refeicaos_update
from .views import refeicaos_delete

from .views import alimentos_list
from .views import alimentos_new
from .views import alimentos_update
from .views import alimentos_delete


urlpatterns = [
    path('list/usuario', usuarios_list, name="usuario_list"),
    path('new/usuario', usuarios_new, name="usuario_new"),
    
    path('list/empresa', empresas_list, name="empresa_list"),
    path('new/empresa', empresas_new, name="empresa_new"),
    path('update/empresa/<int:id>/', empresas_update, name="empresa_update"),
    path('delete/empresa/<int:id>/', empresas_delete, name="empresa_delete"),
    
    path('list/refeicao', refeicaos_list, name="refeicao_list"),
    path('new/refeicao', refeicaos_new, name="refeicao_new"),
    path('update/refeicao/<int:id>/', refeicaos_update, name="refeicao_update"),
    path('delete/refeicao/<int:id>/', refeicaos_delete, name="refeicao_delete"),
    
    path('list/alimento', alimentos_list, name="alimento_list"),
    path('new/alimento', alimentos_new, name="alimento_new"),
    path('update/alimento/<int:id>/', alimentos_update, name="alimento_update"),
    path('delete/alimento/<int:id>/', alimentos_delete, name="alimento_delete"),
]