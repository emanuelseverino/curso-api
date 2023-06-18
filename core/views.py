from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PainelView(TemplateView):
    template_name = 'core/painel.html'
