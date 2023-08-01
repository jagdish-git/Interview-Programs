from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from .models import Account, Post

custom_signal = Signal(['strings','nums'])

def send_req(request):
    custom_signal.send(sender=Post, strings='Custom Strings', nums = '11223344')
    return HttpResponse('This is send request.')


@receiver(request_finished)
def call_after_send_req(sender, **kwargs):
    print('Finished the Request')

@receiver(custom_signal)
def call_before_send_req(sender, **kwargs):
    print(kwargs)

@receiver(post_save, sender=Post)
def afterpostsave(sender, instance, **kwargs):
    return HttpResponse('psotsave')