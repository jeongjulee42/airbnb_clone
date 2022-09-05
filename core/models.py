from django.db import models


class TimeStapedModel(models.Model):
    
    """Time Model Definition"""
    created = models.DateTimeField()
    update = models.DateTimeField()
    
    class Meta:
        abstract = True