from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuario.forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from usuario.models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'username', 'vencimento', 'email', 'celular', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('foto', 'first_name', 'last_name', 'vencimento', 'username', 'celular',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
