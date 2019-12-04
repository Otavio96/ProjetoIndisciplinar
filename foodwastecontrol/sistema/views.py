from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa
from .forms import EmpresaForm

def cadastrar_empresas(request):
    form = EmpresaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('visualizar_empresa')
    return render(request, 'cadastrar_empresa.html', {'form': form})

def visualizar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'visualizar_empresa.html', {'empresas': empresas})