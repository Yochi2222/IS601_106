from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')