from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    translation = models.CharField(max_length=80)
