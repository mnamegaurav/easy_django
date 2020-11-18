from django.urls import path
from mytodo.views import home

urlpatterns = [
    path('', home, name='home'),
]