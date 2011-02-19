from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson




def index(request, **kwargs):

    context = RequestContext(request)

    return render_to_response('pets/map.html', context)

def getdogs(request, **kwargs):
    context = RequestContext(request)
    items = [
        [33.23, 44.45, 'dog', 'http://en.wikipedia.org/wiki/File:YellowLabradorLooking_new.jpg', 3]
    ]

    json = simplejson.dumps(items)

    return HttpResponse(json)
