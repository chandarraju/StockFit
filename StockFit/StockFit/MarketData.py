#!/usr/local/bin/python3.2.1
from urllib import request

class BiVar:

    def __init__(self, tickr):
        self.tickr = tickr

    def fetchClosePrice(self):
        dataSetDict = {}

        dataUrl = "http://www.google.com/finance/getprices?i=900&p=10d&f=d,c&df=cpct&q=" + self.tickr

        sock = request.urlopen(dataUrl)
        htmlSource = sock.read()
        sock.close()

        dataSetAll = htmlSource.split()[7:]
        for item in dataSetAll:
            dateAsKey, price = str(item).split(',')
            if (dateAsKey[2] == 'a'):
                startDay = float(dateAsKey[3:])
                offset = 0
            else:
                offset = float(dateAsKey[2:])

            dateAsKey = (startDay + (offset) * 900)

            dataSetDict[dateAsKey] = str(price[0:-1])
        return dataSetDict

if __name__ == '__main__':

    dataSetDict = {}
    tickr = "MMM"
    print (tickr, end=',')
    company = BiVar(tickr)
    dataSetDict = company.fetchClosePrice()

    fileHandle = open('companyList')
    tickrs = fileHandle.readlines()
    fileHandle.close()
    for tickr in tickrs:
        dataSetDictTemp = {}
        tickr = tickr.rstrip()
        print (tickr, end=',')
        company = BiVar(tickr)
        dataSetDictTemp = company.fetchClosePrice()
        for k1, v1 in dataSetDict.items():
            if k1 in dataSetDictTemp.keys():
                dataSetDict[k1] = str(dataSetDict[k1]) + "," + str(dataSetDictTemp[k1])
            else:
                dataSetDict[k1] = str(dataSetDict[k1]) + "," + "0"
    print(end='\n')

    for k1, v1 in dataSetDict.items():
        print (v1, end='\n')

