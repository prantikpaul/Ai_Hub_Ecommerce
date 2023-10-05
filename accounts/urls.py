from django.urls import path
from .views import sign_in,sign_up,forget_pass

urlpatterns = [
  path('Sign_In/',sign_in,name='sign_inpp'),
  path('Sign_Up/',sign_up,name='sign_uppp'),
  path('Forget_pass/',forget_pass,name='forget_passpp'),
]
