from __future__ import unicode_literals

from django.db import models
from djwslib import joiner

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=16)
    pub = models.ForeignKey(Publisher)

    def __str__(self):
        return self.name
