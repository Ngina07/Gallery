from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image


# Create your views here.

def display_images(request):
    '''
    Method to display all images uploade
    '''
    images = Image.objects.all()

    return render (request, 'images.html',{"images":images})