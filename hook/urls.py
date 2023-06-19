from django.urls import path

from hook.views import WebHookView, PagarView

urlpatterns = [
    path('', WebHookView.as_view(), name='webhook', ),
    path('pagar/', PagarView.as_view(), name='pagar', ),
]
