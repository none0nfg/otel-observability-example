from django.db import models

class Entry(models.Model):
    data = models.CharField(max_length=250)
    expire = models.DateTimeField()
    link = models.URLField(max_length=60, unique=True)
