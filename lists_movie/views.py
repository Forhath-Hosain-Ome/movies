from django.shortcuts import render, redirect
from django.http import HttpRequest

from .forms import moviecreate
from .models import Movies
from typing import Any


# Create your views here.
def home(request:HttpRequest):
    if request.method == "POST":
        form = moviecreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = moviecreate()
    context : dict[str, Any] = {
        'form' : form,
        'movie': Movies.objects.all()
    }
    return render(request, 'lists_movie/home.html',context)