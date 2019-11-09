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

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(categories)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "images":searched_images})

    else:
        message= "Search something.....:)"
        return render(request,'search.html',{"message":message})