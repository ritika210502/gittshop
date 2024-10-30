from django.db import models
from django.utils.html import escape


# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=20,primary_key=True)
    password=models.CharField(max_length=30,null=False)

class product(models.Model):
    
    title=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.FloatField()
    img=models.ImageField(upload_to="ima/%y",blank=True)
    category=models.CharField(max_length=100)
    gender=models.CharField(max_length=30,default="none")
    occasion=models.CharField(max_length=50,default="all")
    def __str__(self):
        return self.title
    


class wishlist(models.Model):
    email=models.EmailField(max_length=20)
    pId=models.IntegerField(null=False)
    
class cart(models.Model):
    email=models.EmailField(max_length=20)
    pId=models.IntegerField(null=False)

