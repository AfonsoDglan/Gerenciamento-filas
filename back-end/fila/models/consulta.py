from django.db import models
from fila.models import Triagem
from fila.models import Pessoa


class Consulta(models.Model):
    paciente = models.ForeignKey(Triagem, editable=False, on_delete=models.PROTECT) # noqa(E501)
    medicoAtendente = models.ForeignKey(Pessoa, editable=False, on_delete=models.PROTECT) # noqa(E501)
    diagnostico = models.TextField('Diagnostico médico', blank=True, null=True)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return self.medicoAtendente
