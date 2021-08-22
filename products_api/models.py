from django.db import models
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
    name = models.CharField(max_length=1000, unique=True)
    password = models.CharField(max_length=1000)

class User(models.Model):
    username = models.CharField(max_length=1000, unique=True)
    password = models.CharField(max_length=1000)
