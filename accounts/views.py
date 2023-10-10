from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def sign_in(request):
    if request.user.is_authenticated:
        return redirect ('indexpp')
    else:
        if request.method=='POST':
            Uname=request.POST['uname']
            Pass=request.POST['pass']
            user=auth.authenticate(username=Uname,password=Pass)
            if user:
                print(user)
                auth.login(request,user)
                messages.success(request, "User Logged In")
                return redirect('indexpp')
            else:
                messages.warning(request,'Invalid Username or password')
        

    return render(request,'accounts/Sign_in.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect ('indexpp')
    else:
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
                        return redirect('sign_inpp')
                    else:
                        messages.warning(request, "Password Must contain atleast 8 letters !!")
                    
            else:
                messages.warning(request, "Your Password Didn't Match !!")


    return render(request,'accounts/Sign_up.html')

def forget_pass(request):

    return render(request,'accounts/Forget_pass.html')

def sign_out(request):
    auth.logout(request)
    messages.success(request, "User Logged Out")
    
    return redirect('indexpp')