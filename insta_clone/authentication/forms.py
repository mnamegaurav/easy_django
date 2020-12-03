from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'username', 'password1', 'password2')