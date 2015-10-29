#
# Kenny Kirtland
# @2015
#
# Stock Ticker Handler class - provides a wrapper for decoupled stock ticker engines
#
#

import json

from StockTickerEngine.StockTickerEngine import StockTickerEngine

class StockTickerHandler(object):

    def __init__(self, stockTickerEngine):
        self.__stockTickerEngine = stockTickerEngine

    def GetStockQuote(self, tickerSymbol):
        """
            Gets the stock quote from the stock ticker engine
        """
        response = self.__stockTickerEngine.GetStockQuote(tickerSymbol)

        return response

    def GetTickerSymbolsFromFile(self, fileName):
        """
            Gets the ticker symbols to be used based off the file name provided in the constructor
        """
        try:
            tickerList = [line.strip() for line in open(fileName, 'r')]
        except FileNotFoundError as err:
            raise FileNotFoundError(str(err))

        return tickerList