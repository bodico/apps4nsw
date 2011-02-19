from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from googlemaps import GoogleMaps
from models import Postcode


def __get_animals(category_id=None):
    items = []

    if category_id:
        animals = Animal.objects.filter(category_id=category_id)
    else:
        animals = Animal.objects.all()

    for animal in animals:
        postcodes = Postcode.objects.filter(postcode=animal.postcode)
        postcode = postcode[0]
        items.append([
            postcode.lat,
            postcode.lon,
            postcode.postcode,
            animal.category_name,
            '/media/img/dogs/' + str(animal.category_id) + '.png',
            animal.counter
        ])

    return items
    


def index(request, **kwargs):

    context = RequestContext(request)

    return render_to_response('pets/map.html', context)

def getdogs(request, **kwargs):

    if request.category_id:
        items = __get_animals(category_id)
    else:
        items = __get_animals()
    

    json = simplejson.dumps(items)

    return HttpResponse(json)
