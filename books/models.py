from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)

class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now=True)