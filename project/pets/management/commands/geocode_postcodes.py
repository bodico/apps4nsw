from django.core.management.base import BaseCommand, CommandError
from project.pets.models import Animal, Postcode
import csv
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        path = os.path.realpath(os.path.dirname(__file__))
        rdr = csv.reader(open(path + '/Australian_Post_Codes_Lat_Lon.csv', 'rb'), delimiter=',', quotechar="\"")
        for row in rdr:
            if i > 0:
                p = Postcode(
                    postcode=row[0],
                    suburb=row[1],
                    state=row[2],
                    dc=row[3],
                    type=row[4],
                    lat=row[5],
                    lon=row[6],
                )
                p.save()
            i += 1
        print "imported " + str(i) + " postcodes"



