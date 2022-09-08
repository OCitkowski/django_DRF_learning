from rest_api.models import Test, CommentTest
from django.contrib.auth.mixins import LoginRequiredMixin

menu = [{'title': "Home", 'url_name': ''},
        {'title': "Tests", 'url_name': 'tests'},
        {'title': "Comments", 'url_name': 'comments'},
        ]


class MixinView():
    model = Test
    paginate_by = 3
    context_object_name = 'tests'

    def get_user_context(self, **kwargs):
        context = kwargs

        context['test_coments'] = CommentTest.objects.all()
        context['menu'] = menu

        return context
