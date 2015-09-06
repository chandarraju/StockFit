'''
Created on Aug 19, 2015

@author: ChandarRaju

This program reads company details from AWS database,
and for each company, searches tweets from Twitter and puts them to database
'''

from TwitterAPI import TwitterAPI
import sys
import codecs

import _mysql

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
        
        con = _mysql.connect('stockfit.ccd1gekitlko.us-west-2.rds.amazonaws.com', 'stockfit', 'stocksfit', 'StockFit')
        
        con.query("SELECT distinct cusip from stk_company")
        result = con.use_result()
        
        print (result.fetch_row())
        
    
    def fetch(self):
        
        api = TwitterAPI(self.consumerKey, self.consumerSecret, self.AccessKey, self.AccessToken, auth_type='oAuth2')
        r = api.request('search/tweets', {'q': 'AAPL', 'count':10, 'result_type': 'recent'})
        
        for item in r:
#            print(item['text'].encode("utf-8") if 'text' in item else item + '\n')
            print(item['id'] if 'text' in item else item + '\n')

allTweets = TweetSearch()
allTweets.fetch()