from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(category)
admin.site.register(product_review)


class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','new_price','category','quantity','trending_prod')
    list_editable=('new_price','trending_prod')

admin.site.register(product,ProductAdmin)

