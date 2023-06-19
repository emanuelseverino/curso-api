import os
import datetime

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from projeto import settings


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PainelView(TemplateView):
    template_name = 'core/painel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione dados adicionais ao contexto, se necessário
        print(datetime.datetime.today() > self.request.user.vencimento)
        context['data_atual'] = datetime.datetime.now()
        context['data_vencimento'] = self.request.user.vencimento
        return context


def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT, 'robots.txt')
    else:
        path = os.path.join(settings.BASE_DIR, 'statics/robots.txt')
    with open(path, 'r') as arq:
        return HttpResponse(arq, content_type="text/plain")


@method_decorator(csrf_exempt, name='dispatch')
class WebHookView(View):
    # @method_decorator(csrf_exempt, name='dispatch')
    # def dispatch(self, request, *args, **kwargs):
    #     return super(WebHookView, self).dispatch(request, *args, **kwargs)  # for python 2
    #     return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        payload = self.request
        if (payload):
            print(request.POST.get('teste'))
            return HttpResponse(status=200)
        return HttpResponse(status=400)
