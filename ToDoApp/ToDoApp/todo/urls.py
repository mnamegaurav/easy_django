from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World!</h1>")


urlpatterns = [
    path('', home, name='home'),
]