from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from googlemaps import GoogleMaps
from models import Postcode, Animal, CategoryPostcodeTotal


def __get_totals(category_id=None):
    items = []

    if category_id:
        totals = CategoryPostcodeTotal.objects.filter(
            category_id=category_id,
            postcode__gte ='2000',
            postcode__lte='2999'
        ).order_by('postcode', 'total')
    else:
        totals = CategoryPostcodeTotal.objects.filter(
            postcode__gte ='2000',
            postcode__lte='2999'
        ).order_by('postcode', 'total')

    for total in totals:
        items.append([
           total.lat,
           total.lon,
           total.postcode,
           total.category_name,
           '/static_media/img/' + str(total.category_id) + '.png',
           total.total
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
2021	570	1	Toy
2022	371	1	Toy
2023	404	1	Toy
2024	415	2	Working
2025	339	1	Toy
2026	777	1	Toy
2027	232	1	Toy
2028	216	1	Toy
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
            '/static_media/img/' + str(catid) + '.png',
            count
        ])

    return items




def index(request, **kwargs):

    context = RequestContext(request)

    return render_to_response('pets/map.html', context)


def getdogs(request, **kwargs):

    items = __get_totals()
    json = simplejson.dumps(items)

    return HttpResponse(json)


def getdogs_category(request, category_id, **kwargs):

    items = __get_totals(category_id)
    json = simplejson.dumps(items)

    return HttpResponse(json)
