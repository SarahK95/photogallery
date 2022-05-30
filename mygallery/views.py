from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image,Category,Location

# Create your views here.


def search_results(request):
    if 'image' in request. GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"message":message,"all_imag": searched_images})
    else:
        message = "You haven't searched for any term"
        return render (request, 'search.html',{"message":message})
