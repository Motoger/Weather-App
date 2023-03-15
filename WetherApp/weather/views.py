from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid= '3722f0cf79a0574960364268f927a658'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)
    context = {'all_info': all_cities,
               'form': form}
    return render(request,'weather/index.html',context)

def new_index(request):
    appid = '3722f0cf79a0574960364268f927a658'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
        'visibility': res["visibility"],
        'humidity': res["main"]["humidity"],
        'pressure': res["main"]["pressure"],
        'name': res["name"],
        'weather': res["weather"][0]["main"],
        'feel': res["main"]["feels_like"],
        'wind': res["wind"]["speed"]
    }
    context = {'info': city_info}
    return render(request,'weather/new_index.html', context)