from django.db import models
from django.urls import reverse


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.ciudad

class Barrio(models.Model):
    ciudad = models.ForeignKey(Ciudad,  on_delete=models.CASCADE)
    barrio = models.CharField(max_length=200)

    def __str__(self):
        return self.barrio

