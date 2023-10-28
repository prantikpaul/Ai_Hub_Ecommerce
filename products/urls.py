from django.urls import path
from . views import prod_page,singl_pro,add_to_cart

urlpatterns = [
    path('all_products/<int:id>/',prod_page,name='all_prod'),
    path('products/<int:id>/',singl_pro,name='single_prod'),
    path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart'),


]
