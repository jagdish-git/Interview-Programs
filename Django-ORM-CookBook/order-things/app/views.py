from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from .models import Hero, Movie, Payment, Temp

import uuid

def temp_obj(request):
    tes = uuid.uuid4()
    temps = Temp.objects.all()
    if temps.count() < 3:
        Temp.objects.create(hy=tes)

    return HttpResponse([i.hy for i in temps])



def create_hero(request):
    h1 = Hero(name='amir', role=4)
    h2 = Hero(name='mahesh', role=6)
    h3 = Hero(name='ranbir', role=3)
    h4 = Hero(name='akshya', role=9)
    try:
        Hero.objects.bulk_create([h1,h2,h3,h4])
    except:
        objs = Hero.objects.values().order_by('name')
        return HttpResponse([i for i in objs])

def get_hero_obj(obj):
    try:
        hero = Hero.objects.all().get(name=str(obj))
    except Hero.DoesNotExist:
        hero = 'Doesnotexist'

    return hero

def create_movie(request):
    m1 = Movie(hero=get_hero_obj('amir'))
    m2 = Movie(title='Bramhastra', hero=get_hero_obj('ranbir'))
    m3 = Movie(title='Rockstar', hero=get_hero_obj('ranbir'))
    m4 = Movie(title='BusinessMan', hero=get_hero_obj('mahesh'))
    m5 = Movie(title='Sooryavansi', hero=get_hero_obj('akshya'))
    m6 = Movie(title='Bachan Pandey', hero=get_hero_obj('akshya'))
    m7 = Movie(title='Bell Botom', hero=get_hero_obj('akshya'))

    try:
        Movie.objects.bulk_create([m1,m2,m3,m4,m5,m6,m7])
    except:
        objs = Movie.objects.order_by('hero__role').values_list()
        return HttpResponse([i for i in objs])

def create_payment(request):
    # p1 = Payment(hero=get_hero_obj('amir'),type='GooglePay')
    p1 = Payment(hero=get_hero_obj('amir'), type='PhonePe')

    try:
        Payment.objects.create(p1)
    except:
        return HttpResponse(Payment.objects.values())




