from django.urls import path
from . views import add_to_cart,show_cart,pay_failed,pay_success,check_out,save_order,add_to_wish_list,show_wish_list


urlpatterns = [
    path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart'),
    path('view_cart/',show_cart,name='show_cart'),
    path('pay_success/',pay_success,name='pay_success'),
    path('pay_failed/',pay_failed,name='pay_failed'),
    path('check_out/',check_out,name='check_out'),
    path('save_order/',save_order,name='save_order'),
    path('add_to_wish_list/<int:id>/',add_to_wish_list,name='add_to_wish_list'),
    path('wishlist/',show_wish_list,name='show_wish_list'),
    
]
