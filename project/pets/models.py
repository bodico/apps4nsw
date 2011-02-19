from django.db import models
from project.glue.models import BaseModel

class Animal(models.Model):
    flavour = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=120, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=120, blank=True, null=True)

class Postcode(models.Model):
    postcode = models.CharField(max_length=120, blank=True, null=True)
    suburb = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    dc = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=80, blank=True, null=True)
    lat = models.CharField(max_length=60, blank=True, null=True)
    lon = models.CharField(max_length=60, blank=True, null=True)
    
