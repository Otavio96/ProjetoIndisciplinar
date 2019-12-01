from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person, Usuario, Empresa, Refeicao, Alimento
from .forms import PersonForm, UsuarioForm, EmpresaForm, RefeicaoForm, AlimentoForm

@login_required
def usuarios_new(request):
    form = UsuarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('usuario_list')
    return render(request, 'cadastrar_usuario.html', {'form': form})
@login_required
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario.html', {'usuarios': usuarios})
@login_required
def usuarios_delete(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_delete_confirm.html', {'usuario': usuario})
@login_required
def empresas_new(request):
    form = EmpresaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('empresa_list')
    return render(request, 'cadastrar_empresa.html', {'form': form})

@login_required
def empresas_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa.html', {'empresas': empresas})

@login_required
def alimentos_new(request):
    form = AlimentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('alimento_list')
    return render(request, 'cadastrar_alimento.html', {'form': form})

@login_required
def alimentos_list(request):
    alimentos = Alimento.objects.all()
    return render(request, 'alimento.html', {'alimentos': alimentos})

@login_required
def alimentos_delete(request, id):
    alimento = get_object_or_404(Alimento, pk=id)
    form = AlimentoForm(request.POST or None, instance=alimento)
    
    if request.method == 'POST':
        alimento.delete()
        return redirect('alimento_list')
    return render(request, 'alimento_delete_confirm.html', {'alimento': alimento})

@login_required
def refeicaos_new(request):
    form = RefeicaoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('refeicao_list')
    return render(request, 'cadastrar_refeicao.html', {'form': form})

@login_required
def refeicaos_list(request):
    refeicaos = Refeicao.objects.all()
    return render(request, 'refeicao.html', {'refeicaos': refeicaos})

@login_required
def refeicaos_delete(request, id):
    refeicao = get_object_or_404(Refeicao, pk=id)
    form = RefeicaoForm(request.POST or None, instance=refeicao)
    
    if request.method == 'POST':
        refeicao.delete()
        return redirect('refeicao_list')
    return render(request, 'refeicao_delete_confirm.html', {'refeicao': refeicao})

@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

@login_required
def persons_new(request):
    form = PersonForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form}) 

@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})
    
