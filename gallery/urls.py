from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('today/',views.gallery_today,name='galleryToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_gallery,name = 'pastGallery'),
    url(r'^image/(\d+)',views.image,name='image')  

]