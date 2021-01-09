from django.db import models
from django.db.models.base import Model

# Create your models here.


class List(Model):
    pass


class Item(Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
