from django.db import models
from django.contrib.auth.models import User
from .ModelMixins import RightsModelRelation,RightsModelMixin



class Address(RightsModelRelation,RightsModelMixin,models.Model):
    lastname = models.CharField(max_length=255, default="", )
    firstname = models.CharField(max_length=255, default="", blank=True, null=True)


