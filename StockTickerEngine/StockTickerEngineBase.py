import abc

class StockTickerEngineBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def GetStockQuote(self, tickerSymbol):
        pass

    @abc.abstractmethod
    def GetTickerSymbolsFromFile(self):
        pass