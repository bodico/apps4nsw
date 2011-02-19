from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext




def index(request, **kwargs):

    context = RequestContext(request)

    return render_to_response('pets/map.html', context)