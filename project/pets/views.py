from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from googlemaps import GoogleMaps
from models import Postcode


def __get_suburbs():
    suburbs = []
    postcodes = Postcode.objects.filter(state='NSW')

    for postcode in postcodes:
        suburbs.append([
            postcode.lat,
            postcode.lon,
            postcode.postcode,
            'SOME_KIND_OF_DOG',
            'http://www.americanrottweiler.org/wp-content/uploads/2009/05/american-rottweiler-puppy.jpg',
            '20'
        ])
    return suburbs
    


def index(request, **kwargs):

    context = RequestContext(request)

    return render_to_response('pets/map.html', context)

def getdogs(request, **kwargs):
    #    context = RequestContext(request)

    #    context['suburbs'] = __fake_suburbs()

    #    items = [
    #        [33.23, 44.45, 'dog', 'http://en.wikipedia.org/wiki/File:YellowLabradorLooking_new.jpg', 3]
    #    ]
    items = __get_suburbs()
    

    json = simplejson.dumps(items)

    return HttpResponse(json)
