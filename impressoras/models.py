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
        return self.nome_dispositivo
    
class Manutencao(models.Model):
    impressora = models.ForeignKey(CadastroImpressora, on_delete=models.CASCADE, related_name='manutencoes')
    data_manutencao = models.DateField(verbose_name="Data da Manutenção")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Concluída', 'Concluída')], default='Pendente', verbose_name="Status")

    def __str__(self):
        return f"{self.impressora.nome_dispositivo} - {self.data_manutencao}"
    
class Departamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Departamento")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.nome
    
class TrocaToner(models.Model):
    impressora = models.ForeignKey(CadastroImpressora, on_delete=models.CASCADE, related_name='trocas_toner')
    data_troca = models.DateField(verbose_name="Data da Troca")
    contador_paginas = models.PositiveIntegerField(default=0, verbose_name="Contador de Páginas")

    def __str__(self):
        return f"{self.impressora.nome_dispositivo} - {self.data_troca}"