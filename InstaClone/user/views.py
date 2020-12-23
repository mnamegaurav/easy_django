from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class ProfileView(View):
    template_name = 'user/profile.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)