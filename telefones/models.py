from django.db import models

class CadastroTelefone(models.Model):
    DEPARTAMENTOS = [
        ('TI', 'TI'),
        ('Financeiro', 'Financeiro'),
        ('RH', 'RH'),
        ('Marketing', 'Marketing'),
        ('Outro', 'Outro'),
    ]

    colaborador = models.CharField(max_length=100, verbose_name="Colaborador")
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, verbose_name="Endereço IP")
    departamento = models.CharField(max_length=50, choices=DEPARTAMENTOS, verbose_name="Departamento")
    status = models.BooleanField(default=True, verbose_name="Status")
    ramal = models.CharField(max_length=10, verbose_name="Ramal")

    def __str__(self):
        return f"{self.name} ({self.ramal})"