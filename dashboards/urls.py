
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [    
    path('tweet_finder/', tweet_finder, name='tweet_finder'),
    path('fetch_tweets_ajax/', fetch_tweets_ajax, name='fetch_tweets_ajax'),
    
    path('data_page/', data_page, name='data_page'),
    path('fetch_data_tweets_ajax/', fetch_data_tweets_ajax, name='fetch_data_tweets_ajax'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 