from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Home(models.Model):
    track_url = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100, blank=True)
    follow = models.BooleanField()
    musicfile = models.FileField(upload_to='music',default='')
    
    def __str__(self):
        return self.track_url

# class Upload(models.Model):
#     musicfile = models.FileField()