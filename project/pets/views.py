from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from googlemaps import GoogleMaps


def __fake_suburbs():
    suburbs = []
    gmaps = GoogleMaps()
    for postcode in range(2000,2010):
        lat, lng = gmaps.address_to_latlng(postcode)
        suburbs.append([
            lat,
            lng,
            postcode,
            'SOME_KIND_OF_DOG',
            'http://en.wikipedia.org/wiki/File:YellowLabradorLooking_new.jpg',
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
    items = __fake_suburbs()
    

    json = simplejson.dumps(items)

    return HttpResponse(json)
