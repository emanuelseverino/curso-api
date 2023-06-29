from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView
from django.contrib import messages

from usuario.forms import CustomUsuarioCreateForm


class CadastroView(CreateView):
    model = get_user_model()
    form_class = CustomUsuarioCreateForm
    template_name = 'usuario/cadastro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha atualizada com sucesso!')
            return redirect('change_password')
        else:
            messages.error(request, 'Digite as informações corretas.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


Usuario = get_user_model()


class AtualizarVencimento(View):

    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(email=self.request.user)
        usuario.atualizar_vencimento()
        usuario.save()
        return HttpResponse(status=200)
