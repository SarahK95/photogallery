from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image,Category,Location

# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{'categories':categories})

def search_results(request):
    if 'image' in request. GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"message":message,"all_imag": searched_images})
    else:
        message = "You haven't searched for any term"
        return render (request, 'search.html',{"message":message})
    
def categoryPage(request, id):
    
    category = Category.objects.get(id=id)
    images = Image.objects.filter(category=category)
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'category.html', context)

def imagePage(request, id):
    
    category = Category.objects.get(id=id)
    image = Image.objects.get(id=id)

    context = {}
    context['category'] = category
    context['image'] = image

    return render(request, 'image.html', context)

# def filter_by_location(request,location_id):
       
#    images = Image.filter_by_location(id=location_id )
#    return render (request, '', {"images":images})
   
