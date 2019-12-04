from django.contrib import admin
from .models import Empresa
from .models import Refeicao
from .models import Desperdicio
from .models import Usuario
from .models import Alimento

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Refeicao)
admin.site.register(Desperdicio)
admin.site.register(Usuario)
admin.site.register(Alimento)