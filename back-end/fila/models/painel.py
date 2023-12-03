from django.db import models
from .pessoa import Pessoa


class Painel(models.Model):
    senha = models.CharField(max_length=220)
    sala = models.CharField(max_length=220)
    quemChamou = models.ForeignKey(Pessoa, on_delete=models.PROTECT) # noqa(E501)
    horaChamada = models.DateTimeField(u'Data e Hora', null=True)

    class Meta:
        verbose_name = "Painel"
        verbose_name_plural = "Paineis"

    def __str__(self):
        return self.senha + self.sala
