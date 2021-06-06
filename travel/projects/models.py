from django.db import models

class City(models.Model):
    city = models.CharField(max_length=100)
    destination = models.CharField(max_length=2000)
    link = models.CharField(max_length=2000)
    linkavia = models.CharField(max_length=2000)
    linkbus = models.CharField(max_length=2000)
    image = models.FilePathField(path="/ img")
