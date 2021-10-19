
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.views.decorators.csrf import csrf_exempt 
import uuid,json,ast,random
from root.models import * 
from .TWEET_FETCHER import  get_all_tweets
 

# Create your views here.

 
@login_required(login_url="login")
def tweet_finder(request): 
    return render(request,'root/search_page.html')

  
def  fetch_tweets_ajax(request):
    username = request.GET['username']
    try:
        incoming_data = get_all_tweets(screen_name=username)
        Tweet_Table.objects.filter(username=username).delete()
        Tweet_Table.objects.bulk_create([
        Tweet_Table(
            username = username,
            text = x['text'],
            created_at = x['created_at'],
            retweet_count = x['retweet_count'],
            like_count = x['like_count'],
            #  reply_count = x['reply_count'],
            #  quote_count = x['quote_count'],
        ) 
        for  x in incoming_data
        ]) 
        return JsonResponse ({
            "data": incoming_data 
        })
    except :
        return JsonResponse ({
            "data": None 
        })
  
  
  
def  data_page(request):
    user_names = list(Tweet_Table.objects.all().distinct().values('username').order_by("username"))
    user_names = [x['username'] for x in user_names]
    print(user_names)
    # Tweet_Table.objects.all().delete()
    return render(request,'root/data_page.html',{'user_names':user_names})  
  
def  fetch_data_tweets_ajax(request):
    username = request.GET['username']
    data =  list(Tweet_Table.objects.filter(username=username).values())
    return JsonResponse({
        "data": data
    })