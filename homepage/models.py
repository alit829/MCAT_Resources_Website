from django.db import models

# Create your models here.

class Postlink(models.Model):
    mcat_redditpost_link = models.CharField(max_length=2083, blank=True)
    dat_redditpost_link =  models.CharField(max_length=2083, blank=True)