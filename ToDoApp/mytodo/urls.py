from django.urls import path
from mytodo.views import home, add_todo

urlpatterns = [
    path('', home, name='home'),
    path('add_todo/', add_todo, name='add_todo'),
]