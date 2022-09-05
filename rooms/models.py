from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class Room(core_models.TimeStapedModel):
    
    """Room Model definition"""
    
    name = models.CharField(max_length=140, null=True)
    description = models.TextField( null=True)
    country = CountryField( null=True)
    city = models.CharField(max_length=80, null=True)
    price = models.IntegerField( null=True)
    address = models.CharField(max_length=140, null=True)
    guests = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    baths = models.IntegerField(null=True)
    check_in = models.TimeField( null=True)
    check_out = models.TimeField( null=True)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
