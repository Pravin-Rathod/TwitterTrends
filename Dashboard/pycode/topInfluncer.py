from .readFetchedTweet import readFetchedTweets
from ..models import Tweet
import pandas as pd

def getTopInfluncer():

    tweets_data = readFetchedTweets()
    tweets = pd.DataFrame()

    tweets['tweet_username'] = [tweet['user'].get('screen_name') for tweet in tweets_data]    
    tweets['tweet_followers_count'] = [tweet['user'].get('followers_count','') for tweet in tweets_data]
    tweets['tweet_profile_image_url'] = [tweet['user'].get('profile_image_url','') for tweet in tweets_data]

    top_fav_tweets = tweets.sort_values('tweet_followers_count',ascending=False)
    top_fav_tweets = top_fav_tweets.reset_index(drop=True)
        
    tweet_obj_list = []

    for i in range(0,5):
        
        tweet_obj = Tweet()
        tweet_obj.tweet_username = top_fav_tweets['tweet_username'][i]
        tweet_obj.tweet_followers_count= top_fav_tweets['tweet_followers_count'][i]
        tweet_obj.tweet_profile_image_url = top_fav_tweets['tweet_profile_image_url'][i]
        tweet_obj_list.append(tweet_obj)

    return tweet_obj_list