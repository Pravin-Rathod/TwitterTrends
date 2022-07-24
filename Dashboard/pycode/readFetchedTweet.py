import json

def readFetchedTweets():
    # BASE_DIR = 'C:\\Users\\BURPY\\Desktop\\TwitterTrends\\'
    # path = BASE_DIR + 'Data/tweets_data.txt'
    path = 'C:\\Users\\PUMBA\\Downloads\\TwitterTrends\\Dashboard\\pycode\\data\\tweets_data.json'
    data = []
    try:
        with open(path,'r') as json_obj:
            data = json.loads(json_obj.read())
    except Exception as e:
        print("Error",e)

    return data