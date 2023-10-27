from django.shortcuts import render
from . models import category,product 

# Create your views here.

def prod_page(request,id):
    cat = category.objects.get(id=id)
    all_prod_of_cat=product.objects.filter(category=cat)
    
        
    return render(request,'products/product.html',locals())

def singl_pro(request,id):
    ppp = product.objects.get(id=id)
    
    

    return render (request,'products/single_prod.html',locals())