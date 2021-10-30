import json
import requests
import dateutil.parser as dparser
import tweepy


consumer_key  = 'XjCEJtii6i9UyWBU8nswv44lX'
consumer_secret  = '6Gw95pc871CpYvugvftWu0pg4j1NFdjS7IqulKqOtF518l4igj'
barer_token='AAAAAAAAAAAAAAAAAAAAABVkUwEAAAAAt2J4EwWzi96t%2FVY3yBi3QVR%2BM%2FU%3DTCig8r6oONYdwZ63P6ThIXOOniCW92kV1IJ8zylOJFhBFH5VZ0'
access_token='1246367267148804096-ttt6yoUldQldfG8HWrP20BMozIpGxW'
access_token_secret='eePClbT5wi3KSB0oB4Lq1O8VsE09UfQMcyxKllj8jJYZJ'





def get_all_tweets(screen_name): 
    print("--> Calling API")
    main_container=[]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth) 
    alltweets = []  
    
    profile_image_url  = api.get_user(screen_name=screen_name).profile_image_url_https
     

    
    
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=200) 
    alltweets.extend(new_tweets) 
    oldest = alltweets[-1].id - 1
     
    while len(new_tweets) > 0: 
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest) 
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        
    # print(alltweets[0]._json)
    print("--> Data Received 100%")
    for data in alltweets:
        data = data._json
        created_at = data['created_at']
        text = data['text']
        # retweeted_status = data['retweeted_status']
        # likes_count = retweeted_status['favorite_count']
        # retweet_count = retweeted_status['retweet_count']
        retweet_count = data['retweet_count']
        likes_count = data['favorite_count']
        created_at = dparser.parse(str(created_at),fuzzy=True).date()
        
        main_container.append(
             {"text": text, "created_at": created_at,
              "retweet_count": int(str(retweet_count)), "like_count": likes_count
              },
        )
  
    return {
            "main_container":main_container,
            "profile_image_url":profile_image_url
        }    

if __name__ == '__main__':
    main_container = get_all_tweets("upasanakonidela")
    # print(main_container[0])

















# def scrape_tweets(username=None):
#     all_tweets = get_all_tweets("abdullahoo433")
#     return all_tweets


# if __name__ == '__main__':
#     print((scrape_tweets()))
