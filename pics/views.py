from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse(request, 'welcome.html')

def pics_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
