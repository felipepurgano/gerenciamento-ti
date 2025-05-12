from django.db import models

# Create your models here.
class CadastroCFTV(models.Model):
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

    def __str__(self):
        return self.nome_dispositivo