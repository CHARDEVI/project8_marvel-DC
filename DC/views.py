from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def batman(request):
    return HttpResponse('<h1>WHY SO SERIOUS</h1>')