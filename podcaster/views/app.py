from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request) -> HttpResponse:
    return render(request, "podcaster/pages/dashboard.html")

def login(request) -> HttpResponse:
    return render(request, "podcaster/pages/auth/login.html")

def register(request) -> HttpResponse:
    return render(request, "podcaster/pages/auth/register.html")

def search(request) -> HttpResponse:
    return render(request, "podcaster/pages/search.html")