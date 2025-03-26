from django.db import models

class CadastroImpressora(models.Model):
    DEPARTAMENTOS = [
        ('TI', 'TI'),
        ('Financeiro', 'Financeiro'),
        ('RH', 'RH'),
        ('Marketing', 'Marketing'),
        ('Outro', 'Outro'),
    ]

    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]

    nome_dispositivo = models.CharField(max_length=100, verbose_name="Nome do Dispositivo")
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, verbose_name="Endereço IP")
    departamento = models.CharField(max_length=50, choices=DEPARTAMENTOS, verbose_name="Departamento")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ativo', verbose_name="Status")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    contador_paginas = models.PositiveIntegerField(default=0, verbose_name="Contador de Páginas")

    def __str__(self):
        return f"{self.nome_dispositivo} ({self.ip})"
