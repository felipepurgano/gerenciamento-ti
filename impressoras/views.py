from django.shortcuts import render, redirect
from .models import CadastroImpressora
from django.contrib import messages
from django.contrib.messages import constants
   
def impressoras(request):
    if request.method == 'GET':
        return render(request, 'impressoras/impressoras.html')

def departamentos(request):    
    if request.method == 'GET':
        return render(request, 'impressoras/departamentos.html')
    
# Função para cadastrar impressora
def cad_impressora(request): 
    if request.method == 'GET':
        return render(request, 'impressoras/cadastro.html')
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
    return redirect('/impressora/cad_impressora')

# # Função para listar impressoras
# def lista_impressoras(request):
#     impressoras = CadastroImpressora.objects.all()
#     return render(request, 'impressoras/impressoras.html', {'impressoras': impressoras})

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

