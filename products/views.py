from django.shortcuts import render,redirect
from . models import category,product,product_review
from cart.models import cart

# Create your views here.

def prod_page(request,id):
    #for search bar ---------------------
    search = request.GET.get('search')
    print(search)
    if search :
        return redirect ('search_prod',search)
    #for search bar ---------------------

    # for showing len of cart in cart button ---------------------------------------
    userP = request.user # getting user
    try:
        if userP.is_authenticated: #if user is logged in
            cart_show=cart.objects.filter(user=userP)[:2]
            len_cart=cart.objects.filter(user=userP) #geting number of cart of that user
            
        a = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            a += i.quantity # getting quantity of each cart and adding them

        b = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            p = i.product.new_price * i.quantity # getting each product and its quantity and multiplying them 
            b += p

    except:
        pass
    # for showing len of cart in cart button ---------------------------------------

    cat = category.objects.get(id=id)
    all_prod_of_cat=product.objects.filter(category=cat)
    
    
        
    return render(request,'products/product.html',locals())

def singl_pro(request,id):
     #for search bar ---------------------
    search = request.GET.get('search')
    print(search)
    if search :
        return redirect ('search_prod',search)
    #for search bar ---------------------
        # for showing len of cart in cart button ---------------------------------------
    userP = request.user # getting user
    try:
        if userP.is_authenticated: #if user is logged in
            cart_show=cart.objects.filter(user=userP)[:2]
            len_cart=cart.objects.filter(user=userP) #geting number of cart of that user
            
        a = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            a += i.quantity # getting quantity of each cart and adding them

        b = 0 # initializing a vallue adding vlaue to it
        for i in len_cart: # in all carts how many items in there
            p = i.product.new_price * i.quantity # getting each product and its quantity and multiplying them 
            b += p

    except:
        pass
    # for showing len of cart in cart button ---------------------------------------

    ppp = product.objects.get(id=id)
    
    rrr = ppp.category # for 15 other products in the same category: 
    prp=str(rrr) # converting category to string


    if prp =='Phone':
        show_prod=product.objects.filter(category='1')
    elif prp=='Laptop':
        show_prod=product.objects.filter(category='2')
    elif prp=='Watch':
        show_prod=product.objects.filter(category='3')
    elif prp=='Food':
        show_prod=product.objects.filter(category='4')
    elif prp=='Tv':
        show_prod=product.objects.filter(category='5')
    elif prp=='Camera':
        show_prod=product.objects.filter(category='6')
    elif prp=='Gadget':
        show_prod=product.objects.filter(category='7')
    elif prp=='Tshirt':
        show_prod=product.objects.filter(category='8')
    elif prp=='Toys':
        show_prod=product.objects.filter(category='9')
    elif prp=='Groceries':
        show_prod=product.objects.filter(category='10')

    if request.POST:
        if request.user.is_authenticated:
        
            try:
                get_star=request.POST['prq']
                get_cmnt=request.POST['comment']
                if get_star and get_cmnt:
                    prod_rev=product_review.objects.create(
                        product=ppp,
                        user=request.user,
                        review_rating=get_star,
                        review_txt=get_cmnt

                        
                    )
                    prod_rev.save()
                    return redirect (request.META['HTTP_REFERER'])
            except:
                pass
        else:
            return redirect ('sign_inpp')
    
    
    ttt=product_review.objects.filter(product=id)
    try:
        for i in ttt:

            if int(i.review_rating) == 5:
                pp_str=5
            elif int(i.review_rating) == 4:
                pp_str=4
            elif int(i.review_rating) == 3:
                pp_str=3
            elif int(i.review_rating) == 2:
                pp_str=2
            elif int(i.review_rating) == 1:
                pp_str=1
    except:
        pass
        
    
    return render (request,'products/single_prod.html',locals())

def search_prod(request,id):
    rr=product.objects.filter(name__icontains=id)
    

    

    return render (request,'products/search.html',locals())


