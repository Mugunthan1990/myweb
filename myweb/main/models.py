from __future__ import unicode_literals #to  adapt all the laguage to the database

from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length = 100, default = '-')
    about = models.TextField(default = '-')
    fb = models.CharField(max_length = 100, default = '-')
    pr = models.CharField(max_length = 100, default = '-')
    tw = models.CharField(max_length = 100, default = '-')
    vi = models.CharField(max_length = 100, default = '-')
    yt = models.CharField(max_length = 100, default = '-')
    tell = models.CharField(max_length = 100, default = '-')
    link = models.CharField(max_length = 100, default = '-')

    set_name = models.CharField(max_length = 100, default = '-')

    def __str__(self):
        return self.set_name + ' | ' + str(self.pk)
