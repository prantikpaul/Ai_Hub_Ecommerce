from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def sign_in(request):

    return render(request,'accounts/Sign_in.html')

def sign_up(request):
    if request.method=='POST':
        Fname=request.POST['fname']
        Lname=request.POST['lname']
        Uname=request.POST['uname']
        Email=request.POST['email']
        Pass=request.POST['pass']
        Cpass=request.POST['cpass']

        if Pass==Cpass:
            if User.objects.filter(username=Uname).exists():
                messages.warning(request, "⚠️ This Username is alreay taken")
            elif User.objects.filter(email=Email).exists():
                messages.warning(request, "⚠️ This email is alreay taken")
            else:
                
                if len(Pass)>7:
                    
                    pp=User.objects.create(
                        first_name=Fname,
                        last_name=Lname,
                        username=Uname,
                        email=Email,
                        password=Pass,
                    )
                    pp.set_password(Pass)
                    pp.save()
                    messages.success(request, "Account Created Successfully")
                else:
                    messages.warning(request, "Password Must contain atleast 8 letters !!")
                
        else:
            messages.warning(request, "Your Password Didn't Match !!")


    return render(request,'accounts/Sign_up.html')

def forget_pass(request):

    return render(request,'accounts/Forget_pass.html')
