from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import URLPattern, path

from . import views
from .pycode import fetch_tweets

urlpatterns = [
    path('fetch_tweets',fetch_tweets.getdata),
    path('Dashboard',views.loadDashboard,name='dashboard'),
    path('Profile',views.loadProfile,name='profile'),
    path('data', views.get_data),
    path('getfetchedtweets',views.loadFetchedTweets,name='fetchedtweets'),
]