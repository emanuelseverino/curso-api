from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import send_mail

from usuario.models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ['email', 'username', 'first_name', 'last_name' ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            #     send_mail(
            #         self.cleaned_data['nome'],
            #         'Se cadastrou',
            #         'emanuel@email.com',
            #         ['emanuelsmseverino@icloud.com', ],
            #         fail_silently=False,
            #     )
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('celular', 'vencimento')
