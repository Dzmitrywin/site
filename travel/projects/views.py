from django.shortcuts import render
from projects.models import City


def cities_index(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, "cities_index.html", context)


def city_detail(request, pk):
    city = City.objects.get(pk=pk)
    context = {"city": city}
    return render(request, "city_detail.html", context)
