from operator import truediv
from django.db import models
class Factory(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
# Create your models here.
class Product(models.Model):
    Factory_name= models.ForeignKey(Factory,on_delete=models.CASCADE)
    Product_name= models.CharField(max_length=200)
    Quantity= models.IntegerField()
    location=models.CharField(max_length=200,null=True)
    description= models.TextField()
    image= models.ImageField(null= True, blank=True,upload_to="images/")
    