from django.db import models

# Create your models here.
class Tweet:
    tweet_userid : str
    tweet_username : str
    tweet_text : str
    tweet_favorite_count : int
    tweet_retweet_count : int
    tweet_followers_count : int
    tweet_profile_image_url :str