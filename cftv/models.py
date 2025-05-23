from django.db import models

# Create your models here.
class CadastroCFTV(models.Model):
    RACKS = [
        ('Sala de cabos', 'Sala de cabos'),
        ('Sala da TI', 'Sala da TI'),
        ('CMU', 'CMU'),
        ('Corredor CMU', 'Corredor CMU'),
        ('Laboratório', 'Laboratório'),
        ('CDU', 'CDU'),
    ]

    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]

    nome_dispositivo = models.CharField(max_length=100, verbose_name="Nome do Dispositivo")
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, verbose_name="Endereço IP")
    rack = models.CharField(max_length=50, choices=RACKS, verbose_name="Rack", default='')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ativo', verbose_name="Status")

    def __str__(self):
        return self.nome_dispositivo