from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name


class product(models.Model):
   name = models.CharField(max_length=50)
   prod_img =models.ImageField(upload_to='product_img/')
   old_price = models.PositiveBigIntegerField()
   new_price = models.PositiveBigIntegerField()
   category = models.ForeignKey(category,on_delete=models.CASCADE)
   quantity = models.IntegerField()
   description = models.TextField()
   trending_prod = models.BooleanField(default=False)
   hot_deal_prod = models.BooleanField(default=False)

   def __str__(self):
      return self.name
   
   