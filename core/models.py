from django.db import models
from . import managers


class TimeStampedModel(models.Model):
    
    """Time Model Definition"""
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()
    
    class Meta:
        abstract = True