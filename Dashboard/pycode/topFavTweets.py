import json
import os
import pandas as pd
from ..models import Tweet
from .readFetchedTweet import readFetchedTweets


def getTopFavTweets():

    tweets_data = readFetchedTweets()
    tweets = pd.DataFrame()

    tweets['tweet_text']= [tweet.get('text','') for tweet in tweets_data]
    tweets['tweet_favorite_count'] = [tweet.get('favorite_count','') for tweet in tweets_data]
    tweets['tweet_profile_image_url'] = [tweet['user'].get('profile_image_url','') for tweet in tweets_data]

    top_fav_tweets = tweets.sort_values('tweet_favorite_count',ascending=False)
    top_fav_tweets = top_fav_tweets.reset_index(drop=True)
        
    tweet_obj_list = []

    for i in range(0,5):
        
        tweet_obj = Tweet()
        tweet_obj.tweet_text = top_fav_tweets['tweet_text'][i]
        tweet_obj.tweet_favorite_count = top_fav_tweets['tweet_favorite_count'][i]
        tweet_obj.tweet_profile_image_url = top_fav_tweets['tweet_profile_image_url'][i]
        tweet_obj_list.append(tweet_obj)

    return tweet_obj_list