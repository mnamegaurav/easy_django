from django.urls import path
from authentication.views import (
    SignInView,
    SignUpView, 
    SignOutView,
    )

urlpatterns = [
    path('',  SignInView.as_view(), name='singin_view'),
    path('signup/',  SignUpView.as_view(), name='singup_view'),
    path('signout/',  SignOutView.as_view(), name='singout_view'),
]