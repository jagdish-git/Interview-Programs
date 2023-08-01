from django.contrib import admin
from django.urls import path
from app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', show_songs),
    path('grp/', aggregate_group),
    path('q/', object_q),
    path('agg', annotate_count),
]
