from django.contrib import admin
from django.urls import path
from app.views import create_hero, create_movie, create_payment, temp_obj


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_hero),
    path('m/', create_movie),
    path('p/', create_payment),
    path('temp/', temp_obj)
]