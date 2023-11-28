from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.mixins import ListModelMixin
from fila.models import Painel
from fila.serializers import PainelSerializer


class PainelConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Painel.objects.all()[:6]
    serializer_class = PainelSerializer
    lookup_field = "pk"

    async def connect(self, **kwargs):
        # You may need to handle disconnect logic here
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(Painel)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=PainelSerializer(instance=instance).data, action=action.value)  # noqa: E501