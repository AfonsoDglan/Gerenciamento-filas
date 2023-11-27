from django.contrib import admin
from fila.models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = [fild.name for fild in Consulta._meta.fields]
