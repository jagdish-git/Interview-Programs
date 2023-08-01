from django.db import models
from django.contrib.auth.models import User


print('----------',User.objects.all())


class Cuser(models.Model):
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)




        