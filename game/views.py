from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def game_view(request):

    # return render(request, 'game/index.html', content_type='application/xhtml+xml')
    # return render(request, 'game/index.html', content_type='text/javascript')
    # View code here...
    t = loader.get_template('game/index.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))


