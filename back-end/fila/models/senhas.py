from django.db import models

STATUS_CHOICES = (
    (1, 'Espera'),
    (2, 'Atendida')
)
TIPO_CHOICES = (
    (1, 'Convencional'),
    (2, 'Preferencial')
)
class Senha(models.Model):
    senha = models.CharField(max_length=20, unique=True)
    status = models.IntegerField('Status', choices=STATUS_CHOICES, null=False)
    tipo = models.IntegerField('Tipo', choices=TIPO_CHOICES, null=False)
    horaEmitida = models.DateTimeField(u'Data e Hora', auto_now_add=True)
    horaChamada = models.DateTimeField(u'Data e Hora', null=True)
    class Meta:
        verbose_name = "Senha"
        verbose_name_plural = "Senhas"

    def __str__(self):
        return self.senha
