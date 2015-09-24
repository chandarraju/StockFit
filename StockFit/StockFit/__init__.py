from StockFit.Company import Company
from StockFit.TweetSearch import TweetSearch

company = Company()

allTweets = TweetSearch()
allTweets.fetch()