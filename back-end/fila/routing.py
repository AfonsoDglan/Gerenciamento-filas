from fila.consumers import PainelConsumer
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r"senhasPainel", PainelConsumer.as_asgi())
]
