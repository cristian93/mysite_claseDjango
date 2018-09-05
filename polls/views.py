from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return  HttpResponse("Ron damon. ");

def name(request):
    return  HttpResponse("Ron damon, te saluda. ");

