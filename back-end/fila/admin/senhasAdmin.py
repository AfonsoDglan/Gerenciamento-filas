from django.contrib import admin
from fila.models import Senha


@admin.register(Senha)
class SenhaAdmin(admin.ModelAdmin):
    list_display = ['senha', 'status', 'tipo']
