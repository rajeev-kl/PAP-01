# django imports
from django.db import models


# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=100)
    gdp = models.CharField(max_length=100)
    population = models.CharField(max_length=20)
    land_area = models.CharField(max_length=20)
    waste_generated = models.CharField(max_length=20)


class UserInfo(models.Model):
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=False, null=False)
