from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=55, primary_key=True)
    duration = models.FloatField()
    size = models.FloatField()
    singer = models.CharField(max_length=77)