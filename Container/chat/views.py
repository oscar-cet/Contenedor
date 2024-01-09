from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Indexview(request):
    return HttpResponse('Hola Mundo!')