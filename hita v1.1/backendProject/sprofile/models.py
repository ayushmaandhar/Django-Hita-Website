from statistics import mode
from typing_extensions import Required
from unicodedata import name
from django.db import models

# Create your models here.
class SignUpForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class agreementsellform(models.Model):
    agree_address = models.CharField(max_length=30,)
    agree_date = models.DateField()
    seller_name = models.CharField(max_length=30 )
    seller_age = models.PositiveIntegerField()
    seller_occ = models.CharField(max_length=30 )
    seller_address = models.CharField(max_length=30 )
    buyer_name = models.CharField(max_length=30 )
    buyer_age = models.PositiveIntegerField()
    buyer_occ = models.CharField(max_length=30 )
    buyer_address = models.CharField(max_length=30 )
    property_address = models.CharField(max_length=30 )
    price = models.PositiveIntegerField()
    token_amount = models.PositiveIntegerField()
    bal_amount = models.PositiveIntegerField()
    bal_date = models.DateField()
    extra_variable = models.DateField()

    def __str__(self):
        return self.seller_name +"_to_"+self.buyer_name







