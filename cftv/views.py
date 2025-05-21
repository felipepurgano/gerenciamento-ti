from django.shortcuts import render, redirect
from .models import CadastroCFTV
from django.contrib import messages
from django.contrib.messages import constants

def cftv(request):
    if request.method == 'GET':
        return render(request, 'cftv/cftv.html')
    
def cad_cftv(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'cftv/cad_cftv.html')
    elif request.method == 'POST':
        nome_dispositivo = request.POST.get('nome_dispositivo')
        ip = request.POST.get('ip')
        rack = request.POST.get('rack')
        status = request.POST.get('status')

    cad_cftv = CadastroCFTV(
        nome_dispositivo=nome_dispositivo,
        ip=ip,
        rack=rack,
        status=status,

    )

    cad_cftv.save()

    messages.add_message(request, constants.SUCCESS, 'DVR cadastrado com sucesso!')
    return redirect('/cftv/cad_cftv/')

def dpto_cftv(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        cftvs = CadastroCFTV.objects.all()
        return render(request, 'cftv/dpto_cftv.html', {'cftvs': cftvs})
    
def equip_cftv(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        dvrs = CadastroCFTV.objects.all()
        return render(request, 'cftv/equip_cftv.html', {'dvrs': dvrs})