from django.db import models
from django.contrib.auth.models import User
from products.models import product

# Create your models here.

class cart(models.Model):
   
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(product, on_delete=models.CASCADE)
   quantity = models.PositiveBigIntegerField(default=1)

   def __str__(self):
      return self.user.username
   
   def total_price(self):
        return self.quantity * self.product.new_price
   

class save(models.Model):
   
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(product, on_delete=models.CASCADE)
   # quantity = models.PositiveBigIntegerField(default=1)

   def __str__(self):
      return self.product.name
   
   def total_price(self):
        return self.quantity * self.product.new_price
   

class order(models.Model):
    Order_status = (
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered')
    )

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_num=models.CharField(max_length=6,blank=True,null=True,)
    order_items=models.ManyToManyField(save)
    total=models.PositiveIntegerField(default=0)
    pay_method=models.CharField(blank=True,null=True,max_length=15)
    order_date=models.DateTimeField(auto_now_add=True)
    order_note=models.CharField(blank=True,null=True,max_length=150)
    paid=models.BooleanField(default=False)
    Order_status=models.CharField(choices=Order_status,default='Pending',max_length=10)

    def __str__(self):
      return self.user.username