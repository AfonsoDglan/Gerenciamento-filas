import json

from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework import permissions
from fila.models.senhas import Senha
from fila.serializers.senhasSerializer import SenhasSerializer

class SenhaConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Senha.objects.all()
    #permission_classes = (permissions.AllowAny)
    serializer_class = SenhasSerializer
    lookup_field = "pk"

    async def connect(self, **kwargs):
    # You may need to handle disconnect logic here
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(Senha)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=SenhasSerializer(instance=instance).data, action=action.value)

    