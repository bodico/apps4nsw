from django.core.management.base import BaseCommand, CommandError
from project.pets.models import Animal, Postcode
import csv
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        animals = Animal.objects.all()
        for animal in animals:
            postcodes = Postcode.objects.filter(postcode=animal.postcode)
            if postcodes:
                postcode = postcodes[0]
                animal.lat = postcode.lat
                animal.lon = postcode.lon
                animal.save()
                i += 1

        print "updated " + str(i) + " records"



