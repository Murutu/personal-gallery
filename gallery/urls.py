from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('today/',views.gallery_today,name='galleryToday'),
]