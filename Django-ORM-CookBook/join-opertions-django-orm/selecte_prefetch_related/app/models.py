from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=77)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=55)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.title
