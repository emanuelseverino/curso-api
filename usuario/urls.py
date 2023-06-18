from django.urls import path, include

from usuario.views import CadastroView

urlpatterns = [
    path('contas/cadastro/', CadastroView.as_view(), name='cadastro-usuario',),
]
