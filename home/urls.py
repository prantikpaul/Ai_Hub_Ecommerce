from django.urls import path
from .views import index,cart_remove
urlpatterns = [
path('',index,name='indexpp'),
path('cart_remove/<int:id>/',cart_remove,name='cart_remove'),
 
]
