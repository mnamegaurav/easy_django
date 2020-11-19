from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    template_name = 'home.html'
    context = {'app_name': "ToDo App"}
    return render(request, template_name, context=context)