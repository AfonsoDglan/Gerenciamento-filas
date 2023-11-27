from django.contrib import admin
from fila.models import Painel


@admin.register(Painel)
class PainelAdmin(admin.ModelAdmin):
    list_display = [fild.name for fild in Painel._meta.fields]
