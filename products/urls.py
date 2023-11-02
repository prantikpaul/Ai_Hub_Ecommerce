from django.urls import path
from . views import prod_page,singl_pro,search_prod

urlpatterns = [
    path('all_products/<int:id>/',prod_page,name='all_prod'),
    path('products/<int:id>/',singl_pro,name='single_prod'),
    path('search_prod/<id>/',search_prod,name='search_prod'),
    


]
