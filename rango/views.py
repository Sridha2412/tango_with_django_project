from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!<br/><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>Ranfo says here is the about page.")
