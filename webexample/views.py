from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h3>Hello World</h3>")

def test(request):
    return HttpResponse("<h3>test</h3>")
