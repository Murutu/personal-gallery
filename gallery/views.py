from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    images = Image.all_images()
    return render(request, 'welcome.html')
    return HttpResponse('Welcome to the Personal Gallery')

# def gallery_of_day(request):
#     date = dt.date.today()
#     html = f'''
#         <html>
#             <body>
#                 <h1> {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)

def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def gallery_today(request):
    date = dt.date.today()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})

   

def past_days_gallery(request,past_date):
    
    def past_days_gallery(request,past_date):
    
        try:
            # Converts data from the string Url
            date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

        except ValueError:
            # Raise 404 error when ValueError is thrown
            raise Http404()
            assert False

    if date == dt.date.today():
        return redirect(gallery_of_day)

    return render(request, 'all-gallery/past-gallery.html', {"date": date})

def image(request,image_id):
    try:
        image=Image.objects.get(id= image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'index.html',{'image':image})

def category(request,category_id):
    try:
        category= Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render (request,'category.html',{'category:category'})

def search_results(request):
    
    if 'photos' in request.GET and request.GET["photos"]:
        category = request.GET.get("photos")
        searched_category = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'all-gallery/search.html',{"message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})