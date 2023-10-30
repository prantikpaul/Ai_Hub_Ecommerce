from django.urls import path
from . views import add_to_cart


urlpatterns = [
    path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart'),
    # path('add_to_cart/',show_cart,name='show_cart'),
]
