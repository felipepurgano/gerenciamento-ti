from django.shortcuts import render, redirect
from .models import CadastroImpressora, Manutencao, Departamento, TrocaToner
from django.contrib import messages
from django.contrib.messages import constants
   
def impressoras(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'impressoras/impressoras.html')

def departamentos(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        departamentos = CadastroImpressora.objects.all()
        return render(request, 'impressoras/departamentos.html', {'departamentos': departamentos})
    
# Função para cadastrar impressora
def cad_impressora(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        departamentos = CadastroImpressora.objects.all()
        return render(request, 'impressoras/cadastro.html', {'departamentos': departamentos})
    elif request.method == 'POST':
        nome_dispositivo = request.POST.get('nome_dispositivo')
        ip = request.POST.get('ip')
        departamento = request.POST.get('departamento')
        status = request.POST.get('status')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        contador_paginas = request.POST.get('contador_paginas')

    cad_impressora = CadastroImpressora(
        nome_dispositivo=nome_dispositivo,
        ip=ip,
        departamento=departamento,
        status=status,
        marca=marca,
        modelo=modelo,
        contador_paginas=contador_paginas
    )

    cad_impressora.save()

    messages.add_message(request, constants.SUCCESS, 'Impressora cadastrada com sucesso!')
    return redirect('/impressora/cad_impressora/')

 # Função para listar impressoras
def lista_impressoras(request):
    impressoras = CadastroImpressora.objects.all()
    return render(request, 'impressoras/listar_equipamentos.html', {'impressoras': impressoras})

def listar_manutencoes(request):
    manutencoes = Manutencao.objects.all()
    return render(request, 'impressoras/dash_manutencoes.html', {'manutencoes': manutencoes})

def manutencoes_imp(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        departamentos = CadastroImpressora.objects.all()
        return render(request, 'impressoras/manutencoes_imp.html', {'departamentos': departamentos})
    
def cadastrar_departamento(request):
    if request.method == 'POST':
        nome = request.POST.get('departamento')
        if nome:
            Departamento.objects.create(departamento=nome)
            return redirect('listar_departamentos')
    return render(request, 'impressoras/cad_dpto_imp.html')

def troca_toner(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        departamentos = CadastroImpressora.objects.all()
        return render(request, 'impressoras/troca_toner.html', {'departamentos': departamentos})
    
def adicionar_troca_toner(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'impressoras/adicionar_troca_toner.html')

# # Função para deletar impressora
# def deleta_impressora(request, id):
#     impressora = CadastroImpressora.objects.get(id=id)
#     impressora.delete()
#     messages.add_message(request, constants.SUCCESS, 'Impressora deletada com sucesso!')
#     return redirect('/impressora/impressoras')

# # Função para editar impressora
# def edita_impressora(request, id):
#     impressora = CadastroImpressora.objects.get(id=id)
#     return render(request, 'impressoras/edita_impressora.html', {'impressora': impressora})

# # Função para atualizar impressora

# def atualiza_impressora(request, id):
#     impressora = CadastroImpressora.objects.get(id=id)
#     impressora.nome_dispositivo = request.POST.get('nome_dispositivo')
#     impressora.ip = request.POST.get('ip')
#     impressora.departamento = request.POST.get('departamento')
#     impressora.status = request.POST.get('status')
#     impressora.marca = request.POST.get('marca')
#     impressora.modelo = request.POST.get('modelo')
#     impressora.contador_paginas = request.POST.get('contador_paginas')
#     impressora.save()
#     messages.add_message(request, constants.SUCCESS, 'Impressora atualizada com sucesso!')
#     return redirect('/impressora/impressoras')