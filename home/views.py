from django.shortcuts import render
from products.models import category

# Create your views here.
def index(request):
        all_cat= category.objects.all()

        return render(request,'home/index.html',locals())