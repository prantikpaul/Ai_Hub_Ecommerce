from django.db import models
from django.contrib.auth.models import User
from products.models import product

# Create your models here.

class cart(models.Model):
   
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(product, on_delete=models.CASCADE)
   quantity = models.PositiveBigIntegerField(default=1)

   def __str__(self):
      return self.user.first_name+''+self.user.last_name
   
   def total_price(self):
        return self.quantity * self.product.new_price
   
    
class Cart_Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amnt=models.FloatField()
    paid_status=models.BooleanField(default=False)
    order_at=models.DateTimeField(auto_now_add=True)
    order_no=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
      return self.user.username

class Order_items(models.Model):
    order=models.ForeignKey(Cart_Order,on_delete=models.CASCADE)
    order_no=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    qyt=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    order_att=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.order.user.username
