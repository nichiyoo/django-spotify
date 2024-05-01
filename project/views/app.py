from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request) -> HttpResponse:
    return render(request, "pages/dashboard.html")

def landing(request) -> HttpResponse:
    return render(request, "pages/auth/landing.html")

def login(request) -> HttpResponse:
    return render(request, "pages/auth/login.html")

def register(request) -> HttpResponse:
    return render(request, "pages/auth/register.html")

def search(request) -> HttpResponse:
    return render(request, "pages/search.html")

def membership(request) -> HttpResponse:
    return render(request, "pages/membership.html")

def player(request) -> HttpResponse:
    return render(request, "pages/player.html")