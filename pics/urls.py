from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.welcome, name='index'),
    path('today/',views.pics_of_day,name='picsToday'),
    path('search/', views.search_results, name='search_results'),
    path('image/(\d+)',views.display_image, name='image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)