from django.urls import path
from user.views import (
    ProfileView,
    ProfileEditView,
    AllProfilesView,
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        'in/<str:username>/', 
        login_required(ProfileView.as_view()), 
        name='profile_view'
        ),
    path(
        'in/<str:username>/edit/', 
        login_required(ProfileEditView.as_view()), 
        name='profile_edit_view'
        ),
    path(
        'profiles/', 
        login_required(AllProfilesView.as_view()), 
        name='all_profiles_view'
        ),
]