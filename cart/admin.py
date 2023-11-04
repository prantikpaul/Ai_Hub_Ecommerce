from django.contrib import admin
from .models import cart,order,save

# Register your models here.

admin.site.register(cart)
admin.site.register(order)
admin.site.register(save)