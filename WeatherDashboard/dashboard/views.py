from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import CityForm
from dashboard.models import City
from dashboard.helper import get_weather_data
# Create your views here.

def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name = form.cleaned_data.get('city_name')
            print(city_name)
            weather_data = get_weather_data(city_name)
    elif request.method == 'GET':
        try:
            city_name = City.objects.latest('date_added').city_name
            weather_data = get_weather_data(city_name)
        except Exception as e:
            weather_data = None

    template_name = 'home.html'
    context = {'form': form, 'weather_data': weather_data}
    return render(request, template_name, context=context)


def history(request):
    template_name = 'history.html'
    cities = City.objects.all().order_by('-date_added')[:5]

    weather_data_list = []
    for city in cities:
        city_name = city.city_name
        weather_data_list.append(get_weather_data(city_name))

    context = {'weather_data_list': weather_data_list}
    return render(request, template_name, context)