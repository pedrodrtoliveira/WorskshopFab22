
from turtle import home
from django.shortcuts import render, redirect
from .models import Cadastro
from Cadastro.models import Cadastro
from .form import CadastroForm

# Create your views here.

def cadastros(request):
    data = {}
    data ['cadastros'] = Cadastro.objects.all()

    return render(request, 'Cadastro/home.html',data)

def novo_cadastro(request):
    data = {}
    form = CadastroForm(request.POST or None)
    data ['form'] = form
    if form.is_valid():
        form.save()

        return redirect('cadastros')

    return render (request, 'Cadastro/cadastro.html', data)

def editar_cadastro(request, pk):
    data = {}
    cadastro = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=cadastro)

    if form.is_valid():
        form.save()
        
        return redirect('cadastros')
    data ['form'] = form
    data ['cadastro'] = cadastro
    return render (request, 'Cadastro/cadastro.html', data)

def apagar(request, pk):
    cadastro = Cadastro.objects.get(pk=pk)
    cadastro.delete()

    return redirect('cadastros')
