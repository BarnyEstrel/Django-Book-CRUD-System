from django.contrib import admin
from .models import Category, Genre
# Register your models here.

admin.site.register(Genre)
admin.site.register(Category)