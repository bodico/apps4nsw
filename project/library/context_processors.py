from django.conf import settings
from documents.models import Link, WebPage, PDF
from itertools import chain
from operator import attrgetter

def settings(request):
    return {
        'SITE_DOMAIN': getattr(settings, 'SITE_DOMAIN', None)
    }

def footer_items(request):
    links_list = [l for l in Link.objects.filter(visible=True)]
    pages_list = [p for p in WebPage.objects.filter(visible=True)]
    pdfs_list  = [p for p in PDF.objects.filter(visible=True)]
    docs_list  = [d for d in QuerySetChain(links, pages, pdfs)]
    result_list = sorted(
        chain(links_list, pages_list, pdfs_list, docs_list),
        key=attrgetter('order'))
        FINISHME!!
    