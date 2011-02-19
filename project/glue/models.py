from datetime import datetime
from django.db import models
from library.utils import slugify

class BaseManager(models.Manager):
    def visible(self, **kwargs):
        return self.filter(visible=True, **kwargs)


class BaseModel(models.Model):
    """
    Fundamental attributes that all bespoke models should have
    """
    visible         = models.BooleanField(default=True, verbose_name='Visible on site')
        
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)
    
    objects = BaseManager()
    
    class Meta:
        abstract = True
    

class OrderedModel(BaseModel):
    
    order                       = models.IntegerField(default=100)
    
    class Meta:
        abstract = True
        ordering = ['order']
        
    
