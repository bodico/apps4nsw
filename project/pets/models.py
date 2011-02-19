from django.db import models
from project.glue.models import BaseModel

class Animal(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=60, blank=True, null=True)
    colour = models.CharField(max_length=120, blank=True, null=True)
    suburb = models.CharField(max_length=120, blank=True, null=True)
    flavour = models.CharField(max_length=200, blank=True, null=True)
    other = models.CharField(max_length=200, blank=True, null=True)

class Postcode(models.Model):
    postcode = models.CharField(max_length=120, blank=True, null=True)
    suburb = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    dc = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=80, blank=True, null=True)
    lat = models.CharField(max_length=60, blank=True, null=True)
    lon = models.CharField(max_length=60, blank=True, null=True)
    
