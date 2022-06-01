from django.shortcuts import render
from .models import Images,Categorys,Locations

# Create your views here.
def home(request):
    categories = Categorys.objects.all()
    images = Images.objects.all()
    return render(request, 'index.html',{'categories':categories, 'images':images })


def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
   
    
def search_location(request):
    location = request.GET.get('location')
    get_location = Images.objects.filter(location_name = location)
    locations = Locations.objects.all()
   
    return render(request, 'location.html', {'location':locations, 'get_location': get_location})

   
