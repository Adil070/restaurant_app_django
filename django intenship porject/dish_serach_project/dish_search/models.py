from django.db import models

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.CharField(max_length=255)
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
