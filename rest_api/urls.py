from django.urls import path
from .views import TestView

app_name = 'blog_urls'
urlpatterns = [
    # ex: /blog
    path('', TestView.as_view(), name='home'),
]