from django.core.management.base import BaseCommand, CommandError
from project.pets.models import Animal, Postcode
import csv
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        j = 0
        path = os.path.realpath(os.path.dirname(__file__))
        rdr = csv.reader(open(path + '/dogs-by-cat-and-suburb.csv', 'rb'), delimiter=',', quotechar="\"")
        for row in rdr:
            if i > 0:
                a = Animal(
                    flavour=row[1],
                    postcode=row[2],
                    counter=row[3],
                    category_id=row[4],
                    category_name=row[5],
                )
                a.save()
                j += 1
            i += 1
        print "imported " + str(j) + " records"



