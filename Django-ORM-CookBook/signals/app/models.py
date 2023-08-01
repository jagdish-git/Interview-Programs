from statistics import mode
from unicodedata import name
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete,pre_delete
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=110)

    def __str__(self):
        return self.title

    
def presave_post(sender, instance, **kwargs):
    print('pre-save method', instance.title)
def postsave_post(sender,instance, **kwargs):
    print('post-save method', instance)
def after_delete_post(sender, instance, **kwargs):
    print('Object Deleted on Post_delete')

post_save.connect(postsave_post, sender=Post)
pre_save.connect(presave_post,sender=Post)
post_delete.connect(after_delete_post, sender=Post)


class Account(models.Model):
    name = models.CharField(max_length=45, null=True,blank=True)
    price = models.IntegerField(default=0)


@receiver(post_save, sender=Post)
def afterpostsave(sender, instance, **kwargs):
    Account(name='Hela', price=499).save()
    print(instance.title)