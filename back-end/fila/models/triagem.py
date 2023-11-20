from django.db import models
from atendimento.models import *
SEXO_CHOICES = (
    (1,'Masculino'),
    (2,'Feminino')
)

DOR_CHOICES = (
    (1,'Sim'),
    (2,'Não')
)

FRATURAS_CHOICES = (
    (1, 'Sim'),
    (2, 'Não')
)

CLASSIFICACAO_CHOICES = (
    (1,'Emergência'),
    (2,'Muito Urgente'),
    (3,'Urgente'),
    (4,'Pouco Urgente'),
    (5,'Não Urgente')
)
ESTADO_CHOICES = (
    (1,'espera'),
    (2,'atendido')
)

class Triagem(models.Model):
    atendente = models.ForeignKey(Pessoa, editable=False, on_delete=models.PROTECT)
    nomePaciente = models.CharField(max_length=220)
    estado = models.IntegerField('Estado da Triagem',choices=ESTADO_CHOICES,null=False)
    senha = models.CharField(max_length=20, null=True, unique=True)
    sexo = models.IntegerField('Sexo', choices=SEXO_CHOICES, null=True) 
    queixaPrincipal = models.TextField('Queixa', blank=True, null=True)
    historicoBreve = models.TextField('Historico', blank=True, null=True) 
    observacaoObjetiva = models.TextField('Observações do Enfermeiro', blank=True, null=True)
    dor = models.IntegerField(verbose_name='Nível de Dor', help_text='De 0 a 10 qual o seu nível de Dor.',choices=[(i, str(i)) for i in range(11)])
    frequenciaCardiaca = models.IntegerField() 
    frequenciaRespiratoria = models.IntegerField()
    pressaoArterial = models.IntegerField()
    temperatura = models.FloatField()
    fraturasExpostas = models.IntegerField('Fraturas Expostas', choices=FRATURAS_CHOICES, null=True) 
    classificacao = models.IntegerField('Classificacao', choices=CLASSIFICACAO_CHOICES, null=True)
    class Meta:
        verbose_name = "Triagem"
        verbose_name_plural = "Triagems"

    def __str__(self):
        return self.nomePaciente

    #def get_absolute_url(self):
    #    return reverse("Triagem_detail", kwargs={"pk": self.pk})
