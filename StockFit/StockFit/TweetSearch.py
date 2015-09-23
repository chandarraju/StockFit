'''
Created on Aug 19, 2015

@author: ChandarRaju

This program searches tweets from Twitter for each company, and puts them to database
'''

from TwitterAPI import TwitterAPI
import sys
import codecs

from StockFit.Company import Company

class TweetSearch:
    
    consumerKey = ""
    consumerSecret = ""
    AccessKey = ""
    AccessToken = ""
    
    tweetId = 0.0
    tweet = ""
    tweetTime = ""
    
    previousLast = 643970505623781376
    lastId = 643970505623781376
    
    def setLastId(self, lastId):
        self.lastId = lastId
        print ("LastID set to", self.lastId)
    
    def __init__(self):
        self.consumerKey = "4Ioh55KdJtNPtQkQfRqXoTw7L"
        self.consumerSecret = "TJjIfThmPwzDLYx1y6zMIFGe6kBFPVA9FYZxfgVtc9YHfq4J4N"
    
    def fetch(self):
        
        count = 0
        
        api = TwitterAPI(self.consumerKey, self.consumerSecret, self.AccessKey, self.AccessToken, auth_type='oAuth2')
        r = api.request('search/tweets', {'q': 'AAPL', 'count':1, 'result_type': 'recent'})
        
        for item in r:
            count+=1
            print(count, item['id'], "\t", item['created_at'] if 'text' in item else item + '\n')
        
        self.lastId = item['id']-1
        temp = item['id']
        
        while self.lastId > (self.previousLast + 1):
            r = api.request('search/tweets', 
                            {'q': 'AAPL', 'count':10, 'result_type': 'recent', 
                             'max_id': self.lastId})
            for item in r:
                count+=1
                print(count, item['id'], "\t", item['created_at'] if 'text' in item else item + '\n')
            print ("Done up to: ", item['id'], "\t", self.lastId, "\t", self.previousLast)
            self.lastId = item['id'] - 1
        self.previousLast = temp
        print ("Done upto ", self.previousLast)

company = Company()

allTweets = TweetSearch()
allTweets.fetch()