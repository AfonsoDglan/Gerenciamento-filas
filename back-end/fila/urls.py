from rest_framework.routers import DefaultRouter
from django.urls import path
from fila.views import (SenhaViewSet, TriagemViewSet,
                        PessoaViewSet, PainelViewSet,
                        ConsultaViewSet)
from django.http import HttpResponse


router = DefaultRouter()
router.register("senhas", SenhaViewSet, basename="senha")
router.register("triagem", TriagemViewSet, basename="triagem")
router.register("pessoa", PessoaViewSet, basename="pessoa")
router.register("painel", PainelViewSet, basename="painel")
router.register("consulta", ConsultaViewSet, basename="consulta")
urlpatters = router.urls


def teste(request):
    return HttpResponse("teste")


urlpatterns = [
    path("", teste),
]
urlpatterns += router.urls
