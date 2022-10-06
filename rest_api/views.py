from django.views.generic import ListView, DetailView, TemplateView

from .serializers import TestSerializer, CommentTestSerializer
from .utils import MixinView
from rest_framework import generics
from .models import Test, CommentTest



class TestView(MixinView, TemplateView):
    template_name = " "

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='about', test='test')
        return context | user_context


class TestApiView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class CommentApiView(generics.ListCreateAPIView):
    queryset = CommentTest.objects.all()
    serializer_class = CommentTestSerializer


