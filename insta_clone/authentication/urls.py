from django.urls import path
from authentication.views import (
    SignInView,
    SignUpView, 
    SignOutView,
    PRView, PRDone, PRConfirm, PRComplete
    )

urlpatterns = [
    path('',  SignInView.as_view(), name='signin_view'),
    path('signup/',  SignUpView.as_view(), name='signup_view'),
    path('signout/',  SignOutView.as_view(), name='signout_view'),
    path('password/reset/', PRView.as_view(), name='password_reset'),
    path('password/reset/done/',  PRDone.as_view() ,name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>', PRConfirm.as_view() , name='password_reset_confirm'),
    path('password/reset/complete/', PRComplete.as_view() , name='password_reset_complete'),
]

# PasswordResetView ->> Ask for Email
# PasswordResetDoneView  ->> Show him success email message
# PasswordResetConfirmView  ->> Ask to set a new password
# PasswordResetCompleteView  ->>  Successfully set your password login