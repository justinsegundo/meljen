from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def services(request):
    return render(request, 'base/services.html')

def contact(request):
    return render(request, 'base/contact.html')