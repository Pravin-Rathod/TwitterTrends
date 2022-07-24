from django.http import JsonResponse
from django.shortcuts import render
from .pycode.analysis import getCountData,getLanguageData,getRtOrgRatio,getTopHashtagData
from .pycode.topFavTweets import getTopFavTweets
from .pycode.topInfluncer import getTopInfluncer
from .pycode.sentiment_analysis import sentence_sentiment
from .pycode.fetchedTweet import getFetchedTweet

# Create your views here.
def loadDashboard(request):
    #keyword = request.GET['keyword']
    total_post, total_user, total_reach = getCountData()
    positive_count , negative_count = sentence_sentiment.getSentiment()
    top_favtweets_tweets = getTopFavTweets()
    top_influencers = getTopInfluncer()
    return render(request,'dashboard.html',{'pv':positive_count,'nv':negative_count,
                 'total_post':total_post,'total_user':total_user,'total_reach':total_reach,
                 'data':top_favtweets_tweets,'influencers':top_influencers})

def loadProfile(request):
    return render(request,'profile.html')

def loadFetchedTweets(request):
    fetched_tweetdata = getFetchedTweet()
    return render(request,'fetchedtweet.html',{'data':fetched_tweetdata})

def get_data(request):
        
    data = []
    languages , languages_count = getLanguageData()
    hashtags , hashtags_count = getTopHashtagData()   
    rtorgRatio = getRtOrgRatio()

    data = {
		'hashtags': hashtags[:10],
		'hashtags_count': hashtags_count[:10],
        
        'languages' : languages[:10],
        'languages_count' : languages_count[:10],

        'rtorgRatio':rtorgRatio,
	}
    
    return JsonResponse(data)