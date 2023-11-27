from django.contrib import admin
from fila.models import Triagem


@admin.register(Triagem)
class TriagemAdmin(admin.ModelAdmin):
    list_display = [fild.name for fild in Triagem._meta.fields]
