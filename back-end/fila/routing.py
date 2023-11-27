from fila.consumers import SenhaConsumer
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r"^ws/$", SenhaConsumer.as_asgi())
]
