from django.shortcuts import render
from . models import category,product 
from cart.models import cart

# Create your views here.

def prod_page(request,id):
    cat = category.objects.get(id=id)
    all_prod_of_cat=product.objects.filter(category=cat)
    
    
        
    return render(request,'products/product.html',locals())

def singl_pro(request,id):
    ppp = product.objects.get(id=id)
    
    rrr = ppp.category # for 15 other products in the same category: 
    prp=str(rrr) # converting category to string


    if prp =='Phone':
        print(rrr)
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
    
    return render (request,'products/single_prod.html',locals())


