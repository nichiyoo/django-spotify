from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return render(request, "pages/playlists/index.html")

def view(request, id) -> HttpResponse:
    return render(request, "pages/playlists/view.html")

def create(request) -> HttpResponse:
    return render(request, "pages/playlists/create.html")