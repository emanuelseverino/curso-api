import os
import datetime

import pytz
from django.http import HttpResponse
from django.utils import timezone
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
        context['data_atual'] = timezone.now()
        context['data_vencimento'] = self.request.user.vencimento
        return context


def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT, 'robots.txt')
    else:
        path = os.path.join(settings.BASE_DIR, 'statics/robots.txt')
    with open(path, 'r') as arq:
        return HttpResponse(arq, content_type="text/plain")
