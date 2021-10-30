
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout 
from django.views.decorators.csrf import csrf_exempt 
import uuid,json,ast,random,requests
from root.models import * 
from .TWEET_FETCHER import  get_all_tweets
from .parameters import  post_url
 

# Create your views here.

 
@login_required(login_url="login")
def tweet_finder(request):  
    return render(request,'root/search_page.html')

  
def  fetch_tweets_ajax(request):
    username = request.GET['username']
    try:
        incoming_data = get_all_tweets(screen_name=username)
        profile_image_url = incoming_data['profile_image_url']
        main_container = incoming_data['main_container']
        
        
         
        Tweet_Table.objects.filter(username=username).delete()
        Tweet_Table.objects.bulk_create([
        Tweet_Table(
            username            = username,
            text                = x['text'],
            created_at          = x['created_at'],
            retweet_count       = x['retweet_count'],
            like_count          = x['like_count'],
            user                = request.user,
            profile_image_url   = profile_image_url
        ) 
        for  x in main_container
        ]) 
        username = request.GET['username']
        data =  list(Tweet_Table.objects.filter(username=username).values())
        return JsonResponse({
        "data": data
    })
    except :
        return JsonResponse ({
            "data": None 
        })
  
  
@login_required(login_url="login")
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
    
    
def import_tweets_to_other_db(request):
    ids = eval(request.GET['ids'])
    if ids:
        ids = [int(str(x)) for  x in ids]
        target_tweets = Tweet_Table.objects.filter(id__in=ids)
        target_tweets.update(imported=True)
        print(ids)
        Imported_Tweet_Table.objects.bulk_create([
            Imported_Tweet_Table(
                username = x.username,
                text = x.text,
                created_at = x.created_at,
                retweet_count = x.retweet_count,
                like_count = x.like_count,
                imported = True,
                user = request.user,
            ) 
            for  x in target_tweets
            ]) 
    
        post_api_data = {}
        if target_tweets:
            twitter_handle = target_tweets.first().username
            twitter_avatar = target_tweets.first().profile_image_url
            tweets = [{
                "message": x.text,
                "date" :x.created_at
            } for x in target_tweets]
            post_api_data['twitter_handle'] = twitter_handle
            post_api_data['twitter_avatar'] = twitter_avatar
            post_api_data['tweets'] = tweets
        try:    
            requests.post(
                post_url,
                data = post_api_data
            )
        except :
            print("Post Api Error !")
        
    
    
    
        username = Tweet_Table.objects.get(id=ids[0]).username
        data =  list(Tweet_Table.objects.filter(username=username).values())
        return JsonResponse({
            "data": data
        })
        