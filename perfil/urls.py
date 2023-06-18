from django.urls import include, path
from rest_framework import routers
from perfil.api.viewsets import PerfilViewSet, RedeSocialViewSet, EnderecoViewSet, LocalizacaoViewSet

router = routers.DefaultRouter()
router.register('', PerfilViewSet)
router.register('redesocial', RedeSocialViewSet)
router.register('endereco', EnderecoViewSet)
router.register('localizacao', LocalizacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
