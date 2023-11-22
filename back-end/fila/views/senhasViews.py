from rest_framework import viewsets
from serializers.senhasSerializer import SenhasSerializer
from models.senhas import Senha
# Create your views here.
# ViewSets define the view behavior.
class SenhaViewSet(viewsets.ModelViewSet):
    queryset = Senha.objects.all()
    serializer_class = SenhasSerializer