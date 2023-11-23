from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "Home.html")


def login(request):
    return render(request, "Log-in.html")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")