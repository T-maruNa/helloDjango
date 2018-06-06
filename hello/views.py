from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django World")

def test(request):
    return HttpResponse("Test, Django World")
