from django.urls import path
from .views import sign_in,sign_up,forget_pass,sign_out,verify_failed,verify_success,verify,verfiy_otp,set_new_pass,update_prof,order_details

urlpatterns = [
  path('Sign_In/',sign_in,name='sign_inpp'),
  path('Sign_Up/',sign_up,name='sign_uppp'),
  path('Forget_pass/',forget_pass,name='forget_passpp'),
  path('sing_out/',sign_out,name='sign_outpp'),
  path('verify_success/',verify_success,name='verify_successpp'),
  path('verify_failed/',verify_failed,name='verify_failedpp'),
  path('verify/<auth_token>/',verify,name='verifypp'),
  path('Forget_pass_otp/',verfiy_otp,name='verfiy_otppp'),
  path('set_new_pass/<int:id>/',set_new_pass,name='set_new_passpp'),
  path('update/<int:id>/',update_prof,name='update_profpp'),
  path('order_details/<id>',order_details,name='order_details'),


]
