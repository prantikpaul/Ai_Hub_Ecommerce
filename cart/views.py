from django.shortcuts import render,redirect
from products.models import product
from .models import cart,order,save
from django.contrib import messages
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt
import random


# Create your views here.
def add_to_cart(request,id):
    prod = product.objects.get(id=id) #user kon product er add to cart a click korse ta oi product er id diye khuje ber kora
    ppppp=product.objects.filter
    

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
            savepp=save.objects.create(user=request.user,product=prod) # creating objects in save class to process data to save user order
            savepp.save()
                
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
        a = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            a += i.quantity # getting quantity of each cart and adding them

        total = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            p = i.product.new_price * i.quantity # getting each product and its quantity and multiplying them 
            total += p
        total_with_shipping=total+100
    except: 
        pass
        
    
        

    return render (request,'cart/view_cart.html',locals())

def check_out(request):
    
    userP = request.user # getting user
    if userP.is_authenticated: #if user is logged in
        len_cart=cart.objects.filter(user=userP) #geting cart objects of that user
        total = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            p = i.product.new_price * i.quantity # getting each product and its quantity and multiplying them 
            total += p
    
    
    sslcz = SSLCOMMERZ({'store_id': 'niyam6412dc52e1e89', 'store_pass': 'niyam6412dc52e1e89@ssl', 'issandbox': True})
    total_amount = total
    data = {
        'total_amount': total_amount,
        'currency': "BDT",
        'tran_id': "tran_12345",
        'success_url': "http://127.0.0.1:8000/cart/save_order/",
        # if transaction is succesful, user will be redirected here
        'fail_url': "http://127.0.0.1:8000/cart/pay_failed/",  # if transaction is failed, user will be redirected here
        # 'cancel_url': "http://127.0.0.1:8000/payment-cancelled",
        # after user cancels the transaction, will be redirected here
        'emi_option': "0",
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general",
    }
    

    response = sslcz.createSession(data)
    return redirect('pay_success')
    # return redirect(response['GatewayPageURL'])
    

    

def pay_success(request):
    # userP = request.user 
    # len_cart=save.objects.filter(user=userP) 
    # quantity = 0
    # list=[]
    # total = 0 
    # for i in len_cart: 
    #     list.append(i.id)
    #     p = i.product.new_price * i.quantity 
    #     total += p
    #     quantity += i.quantity
    
        
    # new_order=order.objects.create(
    #     user=userP,
    #     total=total,
        
        
        
    # )
    # new_order.order_items.set(list)
            
    # new_order.save()
    ## need to work for get the qunatity to save order
    order_numP=random.randint(1111,9999)
    userP = request.user # getting user
    order_save=save.objects.filter(user=userP) 
    len_cart=cart.objects.filter(user=userP) 

    
    
    list=[]
    total = 0 
    for i in order_save: 
        list.append(i.id)
        p = i.product.new_price 
        total += p
        
    
        
        
    
        
    new_order=order.objects.create(
        user=userP,
        total=total,
        order_num=order_numP

        
        
        
    )
    new_order.order_items.set(list)
       
    new_order.save()
#

    
    return render (request,'cart/pay_success.html')














@csrf_exempt
def save_order(request):
    #this func was to born to redirect to success page ... 
    #because if @csrf_exempt is used u cant get request.user.... ! 
    return redirect ('pay_success')

@csrf_exempt
def pay_failed(request):
    
    
    
    return render(request,'cart/pay_failed.html')