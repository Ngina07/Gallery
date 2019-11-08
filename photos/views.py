from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

def welcome(request):
    return render(request, 'images.html')

# Create your views here.
