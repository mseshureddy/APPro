from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def APP1(request):
    return HttpResponse('This is First Application1')