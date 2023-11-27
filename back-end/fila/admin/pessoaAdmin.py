from django.contrib import admin
from fila.models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = [fild.name for fild in Pessoa._meta.fields]
