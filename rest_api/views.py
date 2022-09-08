from django.views.generic import ListView, DetailView, TemplateView
from .utils import MixinView


class TestView(MixinView, TemplateView):
    template_name = " "

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='about', test='test')

        return context | user_context
