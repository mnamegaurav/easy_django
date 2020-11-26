from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import CityForm

import requests

# Create your views here.
def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name = form.cleaned_data.get('city_name')
            print(city_name)

            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=66ff3434ba88fffc04bf3e1812207117&units=metric'
            response = requests.get(url)
            json_response = response.json()

            weather_data = {
                'temp': json_response['main']['temp'],
                'temp_min': json_response['main']['temp_min'],
                'temp_max': json_response['main']['temp_max'],
                'city_name': json_response['name'],
                'country': json_response['sys']['country'],
                'lat': json_response['coord']['lat'],
                'lon': json_response['coord']['lon'],
                'weather': json_response['weather'][0]['main'],
                'weather_desc': json_response['weather'][0]['description'],
                'pressure': json_response['main']['pressure'],
                'humidity': json_response['main']['humidity'],
                'wind_speed': json_response['wind']['speed'],
            }

    elif request.method == 'GET':
        weather_data = None

    template_name = 'home.html'
    context = {'form': form, 'weather_data': weather_data}
    return render(request, template_name, context=context)