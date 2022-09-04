from django.db import models

# Create your models here.
class Factory(models.Model):
    Factory_name= models.CharField(max_length=200)
    Location= models.CharField(max_length=200)
    Product= models.CharField(max_length=200)