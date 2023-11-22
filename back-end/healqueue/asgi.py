import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from fila.routing import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healqueue.settings")

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(websocket_urlpatterns),
})