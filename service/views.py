from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home1(request):
    return render(request,'beforeLogin.html')
    
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def details(request):
    return render(request,'details.html')
