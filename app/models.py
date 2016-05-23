from __future__ import unicode_literals

from django.db import models

class Home(models.Model):
    file = models.FileField(upload_to='music')