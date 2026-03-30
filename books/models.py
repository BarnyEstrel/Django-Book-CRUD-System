from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='books',
        null=True
    )

class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now=True)
