from django.contrib import admin
from django.urls import path

from core.views import IndexView, PainelView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('painel/', PainelView.as_view(), name='painel'),
]
