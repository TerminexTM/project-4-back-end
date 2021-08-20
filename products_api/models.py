from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=32)
    business_name = models.CharField(max_length=32)
    business_id = models.IntegerField()

class Company(models.Model):
    name = models.CharField(max_length=32)
    password = make_password(models.CharField(max_length=32))
