import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def weather_index(request):

	if(request.method == "POST"):
		form = CityForm(request.POST)
		form.save()


	appid = '736784766a099da018015e94b3f188ed'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

	form = CityForm()

	cities = City.objects.all()

	allcities = []

	for city in cities:

		res = requests.get(url.format(city.name)).json()

		cityinfo = {
			'city': city.name,
			'temperature': res["main"]["temp"],
			'icon': res['weather'][0]['icon']
		}

		allcities.append(cityinfo)

	context = {'all_info':allcities, 'form':form}

	return render(request, 'weather_index.html', context)
