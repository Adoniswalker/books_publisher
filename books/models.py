from django.db import models

from authors.models import Authors


class Books(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Authors)
    isbn = models.CharField(max_length=40)
