from .readFetchedTweet import readFetchedTweets
from ..models import Tweet
import pandas as pd

def getFetchedTweet():

    tweets_data = readFetchedTweets()
    tweets = pd.DataFrame()

    tweets['userid']= [tweet.get('id_str','') for tweet in tweets_data]
    tweets['tweet_text']= [tweet.get('text','') for tweet in tweets_data]
    tweets['tweet_favorite_count'] = [tweet.get('favorite_count','') for tweet in tweets_data]
    tweets['tweet_retweet_count'] = [tweet.get('retweet_count','') for tweet in tweets_data]

    tweet_obj_list = []
    
    for i in range(0,100):
        
        tweet_obj = Tweet()
        tweet_obj.tweet_userid = tweets['userid'][i]
        tweet_obj.tweet_text = tweets['tweet_text'][i]
        tweet_obj.tweet_favorite_count = tweets['tweet_favorite_count'][i]
        tweet_obj.tweet_retweet_count = tweets['tweet_retweet_count'][i]
        tweet_obj_list.append(tweet_obj)

    return tweet_obj_list