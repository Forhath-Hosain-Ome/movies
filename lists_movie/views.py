from django.shortcuts import render

# Create your views here.
def home(request):
    return render('lists_movie/home.html')