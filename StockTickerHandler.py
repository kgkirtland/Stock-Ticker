class StockTickerHandler(object):
    def __init__(self, stockTickerEngine):
        self.__stockTickerEngine = stockTickerEngine

    def GetStockQuote(self, tickerSymbol):
        return self.__stockTickerEngine.GetStockQuote(tickerSymbol)

    def GetTickerSymbolsFromFile(self):
        return self.__stockTickerEngine.GetTickerSymbolsFromFile()