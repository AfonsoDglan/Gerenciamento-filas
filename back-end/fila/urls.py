from rest_framework.routers import DefaultRouter
from django.urls import path
from fila.views import (SenhaNomalViewSet, SenhaPrioritariaViewSet,
                        TriagemViewSet, PessoaViewSet,
                        PainelViewSet, ConsultaViewSet)
from django.http import HttpResponse


router = DefaultRouter()
router.register("triagem", TriagemViewSet, basename="triagem")
router.register("pessoa", PessoaViewSet, basename="pessoa")
router.register("painel", PainelViewSet, basename="painel")
router.register("consulta", ConsultaViewSet, basename="consulta")
urlpatters = router.urls


def teste(request):
    return HttpResponse("teste")


urlpatterns = [
    path("", teste),
    path("senhaNormal/", SenhaNomalViewSet.as_view({'get': 'list'})),
    path("senhaPrioritaria/", SenhaPrioritariaViewSet.as_view({'get': 'list'})),
]
urlpatterns += router.urls
