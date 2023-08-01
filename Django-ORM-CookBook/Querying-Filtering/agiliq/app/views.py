from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import Song
from django.db.models import Avg, Max, Min, Sum, Count
from django.db.models import Q


def show_songs(request):
    songs = Song.objects.raw('SELECT * FROM app_song')
    return HttpResponse([x.name for x in songs])


def aggregate_group(request):
    avg = Song.objects.all().aggregate(Avg('size'))
    sum = Song.objects.all().aggregate(Sum('size'))
    count = Song.objects.all().aggregate(Count('size'))
    max = Song.objects.all().aggregate(Max('size'))
    min = Song.objects.all().aggregate(Min('size'))
    return HttpResponse('avg,sum, count, max, min')
       
    
def object_q(request):
    songs = Song.objects.filter(Q(name__startswith='K') | Q(name__endswith='e'))
    songs2 = Song.objects.filter(Q(name__startswith='K') & Q(name__endswith='D'))
    songs3 = Song.objects.filter(Q(name__startswith='L') & ~Q(name__endswith='D'))
    return HttpResponse([x.name+'\t' for x in songs3])
    # return HttpResponse([x.name+'\t' for x in songs2])
    # return HttpResponse([x.name+'\t' for x in songs])

def annotate_count(request):
    song = Song.objects.values('singer').annotate(c =Count('singer')).filter(c = 1)
    duplicate_obj = Song.objects.values('singer').annotate(singer_count=Count('singer')).filter(singer_count__gt=1)
    second_largest_value = Song.objects.order_by('-size').values('name','size')[1]
    print(second_largest_value)
    print([x['singer'] for x in duplicate_obj])
    print([x['singer'] for x in song])
    print([z.name for z in Song.objects.filter(singer__in = [x['singer'] for x in song])])
    return HttpResponse('annotate_count')