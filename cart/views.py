from django.shortcuts import render,redirect
from products.models import product
from .models import cart
from django.contrib import messages


# Create your views here.
def add_to_cart(request,id):
    prod = product.objects.get(id=id) #user kon product er add to cart a click korse ta oi product er id diye khuje ber kora
    

    try:  # try kore dekhbe oi product already cart e ache ki na 
        cart_prod = cart.objects.filter(product=prod)
        
        if cart_prod: # jodi product already thake tahole .... 
                try: # try kore dekhbe single page theke kono quantity send hoy ki na 
                    ttt = int(request.POST['qq']) # geting qunatity from product single page
                    for i in cart_prod:
                        i.quantity += ttt #quantity te single product view page er deowa quantity add korbe .. 
                        i.save()
                except: # signle page theke kono qunatity send na hole .... 
                    for i in cart_prod:
                        i.quantity += 1 # oi exesisting product er sthe quantity 1 add kore dibe 
                        i.save()

        else: 
            add_cart=cart.objects.create(user=request.user , product=prod)
            add_cart.save()
                
    except: # oi oi product already cart e na thake new cart er item create korbe
        messages.warning(request, "To Add Items To Your Cart ,Please Log in")
        return redirect ('sign_inpp')
    
    return redirect (request.META['HTTP_REFERER']) # reload niye protibar same page ei return korbe ... 

def show_cart(request):
    userP = request.user # getting user
    try:
        if userP.is_authenticated: #if user is logged in
            cart_show=cart.objects.filter(user=userP)
            len_cart=cart.objects.filter(user=userP) #geting number of cart of that user
            # if request.method == 'POST':
            #     product_id = request.POST.get('a')
            #     print(product_id)
        a = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            a += i.quantity # getting quantity of each cart and adding them
        print(a)

        total = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            p = i.product.new_price * i.quantity # getting each product and its quantity and multiplying them 
            total += p
        total_with_shipping=total+100
        
        
            



    except: 
        pass
        
    
        

    return render (request,'cart/view_cart.html',locals())