from __future__ import unicode_literals #to  adapt all the laguage to the database

from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length = 100)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length = 12)
    pic = models.TextField()
    writer = models.CharField(max_length = 12)


    def __str__(self):
        return self.name
