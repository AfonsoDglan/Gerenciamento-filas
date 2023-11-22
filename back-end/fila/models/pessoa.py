from django.db import models
from django.contrib.auth.models import User

TIPO_PESSOA_CHOICES = (
    (1, 'Medico'),
    (2, 'Enfermeira')
)

class Pessoa(models.Model):
    cpf = models.CharField('CPF', max_length=11, null=False, unique=True)
    nomeCompleto = models.CharField('Nome Completo', max_length=255)
    user = models.ForeignKey(User, null=False, editable=True, on_delete=models.PROTECT)
    tipo = models.IntegerField('Tipo pessoa', choices=TIPO_PESSOA_CHOICES, null=False)
    sala = models.CharField('Sala', max_length=120, null=False, unique=True)
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nomeCompleto