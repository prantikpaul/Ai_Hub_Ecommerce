from django.urls import path
from . views import prod_page

urlpatterns = [
    path('all_products/<int:id>/',prod_page,name='all_prod'),

]
