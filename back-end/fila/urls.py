from rest_framework.routers import DefaultRouter
from views.senhasViews import SenhaViewSet

router = DefaultRouter()
router.resgister("senhas", SenhaViewSet, basename="senha")

urlpatters = router.urls

urlpatters += [
    
]