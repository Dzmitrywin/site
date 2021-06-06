from django.urls import path
from . import views

urlpatterns = [
    path("", views.cities_index, name="cities_index"),
    path("<int:pk>/", views.city_detail, name="city_detail"),
]
