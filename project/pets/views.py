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


DATA = """
2000	548	1	Toy
2001	4	2	Working
2006	3	2	Working
2007	163	1	Toy
2008	166	1	Toy
2009	275	1	Toy
2010	729	1	Toy
2011	499	1	Toy
2012	1	4	Terrier
2013	1	4	Terrier
2015	410	1	Toy
2016	372	4	Terrier
2017	608	1	Toy
2018	360	1	Toy
2019	413	2	Working
2020	362	4	Terrier
"""


def __dummy_animals(category_id=None):
    items = []

    for line in DATA.strip().split('\n'):
        postcode, count, catid, cat = line.split('\t')
        postcodes = Postcode.objects.filter(postcode=postcode)
        loc = postcodes[0]

        items.append([
            loc.lat,
            loc.lon,
            loc.postcode,
            cat,
            '/media/img/dogs/' + str(catid) + '.png',
            count
        ])

    return items



def index(request, **kwargs):

    context = RequestContext(request)

    return render_to_response('pets/map.html', context)

def getdogs(request, **kwargs):

#    if request.category_id:
#        items = __get_animals(category_id)
#        items = __dummy_animals()
#    else:
        #items = __get_animals()
    items = __dummy_animals()


    json = simplejson.dumps(items)

    return HttpResponse(json)
