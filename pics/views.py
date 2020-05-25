from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image,Location ,Category

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'welcome.html' ,{'images':images})

def pics_of_day(request):
    date = dt.date.today()
    return render(request, 'all-pics/today-pics.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})
    
def display_image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request ,'all-pics/image.html',{"image":image})

