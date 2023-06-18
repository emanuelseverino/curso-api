from django.contrib import admin

from perfil.models import RedeSocial, Endereco, Localizacao

admin.site.register(Endereco)
admin.site.register(RedeSocial)
admin.site.register(Localizacao)
