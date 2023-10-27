from django.shortcuts import render
from products.models import category,product

# Create your views here.
def index(request):
        all_cat= category.objects.all()
        laptop_deal=product.objects.filter(category="2")
        tv_prod=product.objects.filter(category='5')
        smart_phn=product.objects.filter(category='1')
        trnding_prod=product.objects.filter(trending_prod=True)
        

        return render(request,'home/index.html',locals())

