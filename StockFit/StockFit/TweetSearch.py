'''
Created on Aug 19, 2015

@author: ChandarRaju
'''

from TwitterAPI import TwitterAPI
import sys
import codecs

class TweetSearch:
    
    consumerKey = ""
    consumerSecret = ""
    AccessKey = ""
    AccessToken = ""
    
    tweetId = 0.0
    tweet = ""
    tweetTime = ""
    
    def __init__(self):
        self.consumerKey = "4Ioh55KdJtNPtQkQfRqXoTw7L"
        self.consumerSecret = "TJjIfThmPwzDLYx1y6zMIFGe6kBFPVA9FYZxfgVtc9YHfq4J4N"
    
    def fetch(self):
        
        api = TwitterAPI(self.consumerKey, self.consumerSecret, self.AccessKey, self.AccessToken, auth_type='oAuth2')
        r = api.request('search/tweets', {'q': 'AAPL', 'count':100, 'result_type': 'recent'})
        
        for item in r:
#            print(item['text'].encode("utf-8") if 'text' in item else item + '\n')
            print(item['id'] if 'text' in item else item + '\n')

allTweets = TweetSearch()
allTweets.fetch()