from django.shortcuts import render,redirect
from products.models import product
from .models import cart


# Create your views here.
def add_to_cart(request,id):
    prod = product.objects.get(id=id) #user kon product er add to cart a click korse ta oi product er id diye khuje ber kora
    

    try:  # try kore dekhbe oi product already cart e ache ki na 
        cart_prod = cart.objects.filter(product=prod)
        
        if cart_prod: # jodi product already thake tahole .... 
                try: # try kore dekhbe single page theke kono quantity send hoy ki na 
                    ttt = int(request.POST['qq']) # geting qunatity from product single page
                    for i in cart_prod:
                        i.quantity += ttt
                        i.save()
                except: # signle page theke kono qunatity send na hole .... 
                    for i in cart_prod:
                        i.quantity += 1 # oi exesisting product er sthe quantity 1 add kore dibe 
                        i.save()

        else: 
            add_cart=cart.objects.create(user=request.user , product=prod)
            add_cart.save()
                
    except: # oi oi product already cart e na thake new cart er item create korbe
        add_cart=cart.objects.create(user=request.user , product=prod) # request.user = bolte akhne kon user logged in asey ta get korbe
        add_cart.save()
    
    return redirect (request.META['HTTP_REFERER']) # reload niye protibar same page ei return korbe ... 