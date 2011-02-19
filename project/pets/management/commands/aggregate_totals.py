from django.core.management.base import BaseCommand, CommandError
from project.pets.models import Animal, Postcode, CategoryPostcodeTotal

class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        animals = Animal.objects.all()
        for animal in animals:
            try:
                cpt = CategoryPostcodeTotal.objects.get(
                    category_id=animal.category_id,
                    postcode=animal.postcode
                )
                cpt.total += animal.counter
            except:
                cpt = CategoryPostcodeTotal(
                    category_id = animal.category_id,
                    category_name = animal.category_name,
                    postcode = animal.postcode,
                    total = animal.counter,
                    lat = animal.lat,
                    lon = animal.lon
                )
                i += 1
            cpt.save()


        print "created " + str(i) + " category postcode total records"



