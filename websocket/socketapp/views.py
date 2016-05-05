from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django_sse.redisqueue import RedisQueueView

class HomePage(TemplateView):
    template_name = 'index.html'

    class SSE(RedisQueueView):
        pass
