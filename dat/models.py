from django.db import models

choice = [("Free", "Free"), ("Paid", "Paid")]

class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=400, blank=True)
    material_link = models.CharField(max_length=2083, blank=True)
    web_link = models.CharField(max_length=2083, blank=True)
    is_it_free = models.TextField(choices=choice)