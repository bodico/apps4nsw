from django.db import models
from project.glue.models import BaseModel

class Animal(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=60)
    colour = models.CharField(max_length=120)
    suburb = models.CharField(max_length=120)
    flavour = models.CharField(max_length=200)
    other = models.CharField(max_length=200)

class Postcode(models.Model):
    postcode = models.CharField(max_length=120)

    
