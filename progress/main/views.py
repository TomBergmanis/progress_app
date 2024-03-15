from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required 
from .models import Homepage

# Create your views here.

def index(response):
    return render(response, "main/base.html", {"name": "Test"})

def home(response):
    return render(response, "main/home.html", {"name": "Home page"})

def progress(response):
    return render(response, "main/progress.html", {"name": "Progress"})