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
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "images":searched_images})

    else:
        message= "Search something.....:)"
        return render(request,'search.html',{"message":message})