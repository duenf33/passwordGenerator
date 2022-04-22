from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Hi there...General Kenobi')
    return render(request, 'generator/home.html')

def password(request):
    return render(request, 'generator/password.html', {'password': 'fernando'})

def about(request):
    return render(request, 'generator/about.html')