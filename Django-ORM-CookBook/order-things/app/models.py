from pyexpat import model
from django.contrib.auth.models import User
from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=55, primary_key=True)
    role = models.IntegerField(null=True, blank=True, db_column='role in movie')

    def __str__(self):
        return self.role

class Movie(models.Model):
    title = models.CharField(max_length=55, primary_key=True)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)


class Payment(models.Model):     
    hero = models.OneToOneField(Hero, on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(max_length=33)

class Heroin(models.Model):
    hname = models.CharField(max_length=55, primary_key=True)
    hero = models.ManyToManyField(Hero)


import uuid

class Temp(models.Model):
    hy = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)


from django.utils.text import slugify

class Slugo(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Slugo, self).save(*args, **kwargs)
