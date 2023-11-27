# Generated by Django 4.2.3 on 2023-11-27 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fila', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('nomeCompleto', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('tipo', models.IntegerField(choices=[(1, 'Medico'), (2, 'Enfermeira')], verbose_name='Tipo pessoa')),
                ('sala', models.CharField(max_length=120, unique=True, verbose_name='Sala')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Triagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePaciente', models.CharField(max_length=220)),
                ('estado', models.IntegerField(choices=[(1, 'espera'), (2, 'atendido')], verbose_name='Estado da Triagem')),
                ('senha', models.CharField(max_length=20, null=True, unique=True)),
                ('sexo', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')], null=True, verbose_name='Sexo')),
                ('queixaPrincipal', models.TextField(blank=True, null=True, verbose_name='Queixa')),
                ('historicoBreve', models.TextField(blank=True, null=True, verbose_name='Historico')),
                ('observacaoObjetiva', models.TextField(blank=True, null=True, verbose_name='Observações do Enfermeiro')),
                ('dor', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], help_text='De 0 a 10 qual o seu nível de Dor.', verbose_name='Nível de Dor')),
                ('frequenciaCardiaca', models.IntegerField()),
                ('frequenciaRespiratoria', models.IntegerField()),
                ('pressaoArterial', models.IntegerField()),
                ('temperatura', models.FloatField()),
                ('fraturasExpostas', models.IntegerField(choices=[(1, 'Sim'), (2, 'Não')], null=True, verbose_name='Fraturas Expostas')),
                ('quimadurasGraves', models.ImageField(choices=[(1, 'Sim'), (2, 'Não')], upload_to='', verbose_name='Queimaduras Graves.')),
                ('classificacao', models.IntegerField(choices=[(1, 'Emergência'), (2, 'Muito Urgente'), (3, 'Urgente'), (4, 'Pouco Urgente'), (5, 'Não Urgente')], null=True, verbose_name='Classificacao')),
                ('atendente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='fila.pessoa')),
            ],
            options={
                'verbose_name': 'Triagem',
                'verbose_name_plural': 'Triagems',
            },
        ),
        migrations.CreateModel(
            name='PainelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chamado', models.CharField(max_length=220)),
                ('horaChamada', models.DateTimeField(null=True, verbose_name='Data e Hora')),
                ('quemChamou', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='fila.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(blank=True, null=True, verbose_name='Diagnostico médico')),
                ('medicoAtendente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='fila.pessoa')),
                ('paciente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='fila.triagem')),
            ],
        ),
    ]