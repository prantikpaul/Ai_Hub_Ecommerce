from django.shortcuts import render

# Create your views here.

def sign_in(request):

    return render(request,'accounts/Sign_in.html')

def sign_up(request):

    return render(request,'accounts/Sign_up.html')

def forget_pass(request):

    return render(request,'accounts/Forget_pass.html')
