from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'hello.html')

def test(request):
    return HttpResponse("Test, Django World")
