from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStapedModel):
    
    """Abstract Item"""

    name = models.CharField(max_length=30)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name
    


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    pass


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    pass


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    pass


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
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)
    
    def __str__(self):
        return self.name
