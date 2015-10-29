#
# Kenny Kirtland
# @2015
#
# Stock Ticker Engine Base provides an abstract base class for stock ticker engines
#
#

import abc

class StockTickerEngineBase(object):
    """
        This class provides a set of methods to be overidden by a stocker ticker engine
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def GetStockQuote(self, tickerSymbol):
        pass

    @abc.abstractmethod
    def GetTickerSymbolsFromFile(self):
        pass