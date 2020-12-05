from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from authentication.forms import UserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_feed')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, self.template_name) 
        login(request, user)
        return redirect('home_feed')
        


class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_feed')
        # ye wala code run kardo
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # ye wala code run kardo
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singin_view')

        context = {'form': form}

        return render(request, self.template_name, context)


class SignOutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('singin_view')
