from django.urls import path
from .import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloWarudo.as_view()),
    path('genre', views.home),
]