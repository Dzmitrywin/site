from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_index, name="contact_index"),
]
