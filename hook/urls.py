from django.urls import path

from hook.views import WebHookView, PagarView, TesteView

urlpatterns = [
    path('', WebHookView.as_view(), name='webhook', ),
    path('pagar/', PagarView.as_view(), name='pagar', ),
    path('teste/', TesteView.as_view(), name='teste', ),
]
