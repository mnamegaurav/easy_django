from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")


urlpatterns = [
    path('', home, name='home'),
]