from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# -----------for forget pass -------------
from django.contrib.auth import update_session_auth_hash
import random
#---------------for email verify---------------------------
import uuid
from django.core.mail import send_mail
from .models import Profile
from django.conf import settings


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
                prof=Profile.objects.get(user=user) #profile er nam & user er nam same
                if prof.is_verified is True or prof.sign_in_otp_verify is True:

                    print(user)
                    auth.login(request,user)
                    messages.success(request, "User Logged In")
                    return redirect('indexpp')
                else:
                    messages.warning(request,'Please Verify Your Mail')
                    return redirect('verify_successpp')
            else:
                messages.warning(request,'Invalid Username or password')
        

    return render(request,'accounts/Sign_in.html')

def sign_up(request):
    otpp = random.randint(111111,999999)
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
                        
                        auth_token = str(uuid.uuid4())

                        pro_obj = Profile.objects.create(user=pp, auth_token=auth_token,otp=otpp) #creatig a profile on this user
                        pro_obj.save()
                        send_mail_registration(Email, auth_token,otpp)
                        return redirect ('verify_successpp')
                        # messages.success(request, "Account Created Successfully")
                        # return redirect('sign_inpp')
                    else:
                        messages.warning(request, "Password Must contain atleast 8 letters !!")
                    
            else:
                messages.warning(request, "Your Password Didn't Match !!")


    return render(request,'accounts/Sign_up.html')



def sign_out(request):
    auth.logout(request)
    messages.success(request, "User Logged Out")
    
    return redirect('indexpp')



def verify_success(request):
    if request.method=='POST':
        otpp = request.POST['otp']
        ppr=Profile.objects.get(otp=otpp)
        # print(ppr)
        # print(otpp)
        if ppr :
            ppr.sign_in_otp_verify= True
            ppr.save()
            messages.success(request,'Your Email Verified Successfully')
            return redirect ('sign_inpp')
            

    
    return render(request,'accounts/verify_success.html')

def verify_failed(request):
    
    return render(request,'accounts/verify_failed.html')

def send_mail_registration(Email, token,otpp):
    subject = "Account Verification link"
    message = f'hi click the link for verify http://127.0.0.1:8000/accounts/verify/{token}\n\n\n Or You can use this OTP :{otpp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    profile_obj.is_verified = True
    profile_obj.save()
    messages.success(request, 'OWWO,your mail is verified')
    return redirect('sign_inpp')

def verify_sign_in_otp(request):
    
    pass

def forget_pass(request):
    otp=random.randint(111111,999999)
    if request.method=='POST':
        Email=request.POST['email']
        
        if Email :
            try:
                pp = User.objects.get(email=Email) #email diye user name ber kora
                if pp:
                    # print(pp)
                    rr = Profile.objects.get(user=pp) #username diye profile ber kora
                    rr.otp=otp
                    rr.save()
                    send_mail_forget_pass(Email,otp)
                    
                    # print(rr)

                    return redirect('verfiy_otppp')

            except:
                messages.warning(request,"No User Found !!")
        

        
                
        else:
            messages.warning(request,"Email Didn't matached")
        # return redirect('verfiy_otppp')

    return render(request,'accounts/Forget_pass.html')

def send_mail_forget_pass(Email, otp):
    subject = "Account Verification link"
    message = f'Hi this is your OTP : {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def verfiy_otp(request):
    if request.method=='POST':
        OTP=request.POST['otp']
        if OTP:
            try:
                pp = Profile.objects.get(otp=OTP)
                # print(pp)
                if pp :
                    return redirect('set_new_passpp')
                
            except:
                messages.warning(request,"OTP Didn't matached")
        else:
            messages.warning(request,"Please Enter Your OTP")
    
    return render (request,'accounts/Forget_pass_otp.html')

def set_new_pass(request):
    if request.method=='POST':
        Pass=request.POST['pass']
        Cpass=request.POST['cpass']
        if Pass and Cpass :
            if Pass==Cpass:
                pass

    
    return render (request,'accounts/set_new_pass.html')