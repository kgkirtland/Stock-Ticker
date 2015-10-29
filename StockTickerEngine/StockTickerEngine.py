import requests
import json

from StockTickerEngineBase import StockTickerEngineBase

class StockTickerEngine(StockTickerEngineBase):
    __statusCodeOk = 200

    def __init__(self, url, tickerFileName):
        self.__url = url
        self.__fileName = tickerFileName
    
    def GetStockQuote(self, tickerSymbol):           
        request = requests.get(self.__url % tickerSymbol)

        if request.status_code != self.__statusCodeOk:
            return 
   
        lines = request.content.splitlines()

        return json.loads(''.join([x for x in lines if x not in ('// [', ']')]))

    def GetTickerSymbolsFromFile(self):        
        tickerList = [line.strip() for line in open(self.__fileName, 'r')]

        return tickerList
