from django.shortcuts import render,redirect
from products.models import category,product
from cart.models import cart

# Create your views here.
def index(request):
    all_cat= category.objects.all()
    laptop_deal=product.objects.filter(category="2")
    tv_prod=product.objects.filter(category='5')
    smart_phn=product.objects.filter(category='1')
    trnding_prod=product.objects.filter(trending_prod=True)

    # for showing len of cart in cart button
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
    
     #for search bar ---------------------
    search = request.GET.get('search')
    print(search)
    if search :
        return redirect ('search_prod',search)
    #for search bar ---------------------
    


    
    
    return render(request,'home/index.html',locals())

def cart_remove(request,id):  #cart er X button click korle product remove kore dibe ... 
    ppq=cart.objects.filter(user=request.user , product=id)
    for i in ppq:
        i.delete()

    return redirect('indexpp')
