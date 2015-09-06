import pyodbc

import pandas as pd
from datetime import timedelta
import math

# import numpy as np
# from pandas.io.data import DataReader
# from datetime import datetime
# import scipy.stats  as stats

class Correlation:

    correlationData = {}
    correlationTotal = {}
    correlationPos = {}
    correlationNeg = {}

    cusip=23135106

    cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER=QTDFPDBDV01.ciqdev.com; DATABASE=TweetVestors; UID=MissionPossible2015; PWD=Team2')
    cursor = cnxn.cursor()

    cursor.execute("select distinct DATE from [TweetVestors].[dbo].[StockDataHourly_tbl] where Cusip = ? and Date > '2015-07-07 08:00:00.000' order by DATE", cusip)
    dateRows= cursor.fetchall()

    for eachDate in dateRows:

        newDate = eachDate.DATE - timedelta(days=4)

        cursor.execute("select * from [TweetVestors].[dbo].[TweetStatsHourly_tbl] where Cusip = ? and date <= ? and date >=?", cusip, eachDate.DATE, newDate)

        rows = cursor.fetchall()
        Rating = {}
        TotalTweets = {}
        PositiveTweets = {}
        NegativeTweets = {}

        for x in rows:
            Rating[x.Date] = x.Rating
            TotalTweets[x.Date] = x.TotalTweets
            PositiveTweets[x.Date] = x.PositiveTweets
            NegativeTweets[x.Date] = x.NegativeTweets

        cursor.execute("select * from [TweetVestors].[dbo].[StockDataHourly_tbl] where Cusip = ?", cusip)

        stockRows = cursor.fetchall()
        StockPrice = {}

        for x in stockRows:
            StockPrice[x.Date] = x.StockPrice

        df1 = pd.Series(Rating.values(), index=Rating.keys())
        df2 = pd.Series(StockPrice.values(), index=StockPrice.keys())

        dfTot = pd.Series(TotalTweets.values(), index=TotalTweets.keys())
        dfPos = pd.Series(PositiveTweets.values(), index=PositiveTweets.keys())
        dfNeg = pd.Series(NegativeTweets.values(), index=NegativeTweets.keys())

        correlationData[eachDate.DATE] = df1.corr(df2)
        correlationTotal[eachDate.DATE] = dfTot.corr(df2)
        correlationPos[eachDate.DATE] = dfPos.corr(df2)
        correlationNeg[eachDate.DATE] = dfNeg.corr(df2)

    for cd in correlationData:
        if not math.isnan(correlationData[cd]):
            cursor.execute("insert into Correlation_tbl(cusip, date, PriceToRating) values (?, ?, ?)", cusip, cd, round(correlationData[cd], 3))
            cnxn.commit()

    for cdTot in correlationTotal:
        if not math.isnan(correlationTotal[cdTot]):
            cursor.execute("update Correlation_tbl set PriceToTotal = ? where cusip = ? and date = ?", round(correlationTotal[cdTot], 3), cusip, cdTot)
            cnxn.commit()

    for cdPos in correlationPos:
        if not math.isnan(correlationPos[cdPos]):
            cursor.execute("update Correlation_tbl set PriceToPositive = ? where cusip = ? and date = ?", round(correlationPos[cdPos], 3), cusip, cdPos)
            cnxn.commit()

    for cdNeg in correlationNeg:
        if not math.isnan(correlationNeg[cdNeg]):
            cursor.execute("update Correlation_tbl set PriceToNegative = ? where cusip = ? and date = ?", round(correlationNeg[cdNeg], 3), cusip, cdNeg)
            cnxn.commit()

