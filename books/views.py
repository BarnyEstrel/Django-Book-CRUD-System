from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import GenreForm
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

class HelloWarudo(View):
    def get(self, request):
        return HttpResponse("Hello Warudo")

def home(request):
    form = GenreForm()

    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    return render(request, 'index.html', {'form' : form})