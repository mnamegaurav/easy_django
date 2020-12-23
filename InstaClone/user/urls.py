from django.urls import path
from user.views import (
    ProfileView
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<str:username>/', login_required(ProfileView.as_view()), name='profile_view'),
]