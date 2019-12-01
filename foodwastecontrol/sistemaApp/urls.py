from django.urls import path
from .views import usuarios_list
from .views import usuarios_new
from .views import usuarios_delete

from .views import empresas_list
from .views import empresas_new

from .views import refeicaos_list
from .views import refeicaos_new
from .views import refeicaos_delete

from .views import alimentos_list
from .views import alimentos_new
from .views import alimentos_delete

from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete

urlpatterns = [
    path('list/usuario', usuarios_list, name="usuario_list"),
    path('new/usuario', usuarios_new, name="usuario_new"),
    path('delete/usuario/<int:id>/', usuarios_delete, name="usuario_delete"),
    
    path('list/empresa', empresas_list, name="empresa_list"),
    path('new/empresa', empresas_new, name="empresa_new"),
    
    path('list/refeicao', refeicaos_list, name="refeicao_list"),
    path('new/refeicao', refeicaos_new, name="refeicao_new"),
    path('delete/refeicao/<int:id>/', refeicaos_delete, name="refeicao_delete"),
    
    path('list/alimento', alimentos_list, name="alimento_list"),
    path('new/alimento', alimentos_new, name="alimento_new"),
    path('delete/alimento/<int:id>/', alimentos_delete, name="alimento_delete"),
    
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]