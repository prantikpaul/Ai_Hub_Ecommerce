from django.contrib import admin
from .models import cart,Order_items,Cart_Order

# Register your models here.

admin.site.register(cart)

admin.site.register(Cart_Order)
class Order_itemsAdmin(admin.ModelAdmin):
    list_display=('order','order_att')
admin.site.register(Order_items,Order_itemsAdmin)