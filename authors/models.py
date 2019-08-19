from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    date_stated_writing = models.DateField()
