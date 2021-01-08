from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
# Create your views here.


def home(request):

    site = Main.objects.get(pk = 1)
    news = News.objects.all()
    # site = Main.objects.filter(pk = 2) #need for loop

    return render(request, "front/home.html" , {'site':site, 'news': news})

def about(request):
        # site = Main.objects.filter(pk2)
    site = Main.objects.get(pk = 1)
    # sitename = "Mysite | About"
    return render(request, "front/about.html", {'site':site})


def panel(request):

    return render(request, "back/home.html")
