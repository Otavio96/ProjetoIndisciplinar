from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request, 'index.html')

def cadastarEmpresa(request):
   return render(request, 'cadastrar_empresa.html')