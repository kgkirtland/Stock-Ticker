#
# Kenny Kirtland
# @2015
#
# Stock Ticker Manager class - provides front-end functions
#
#

import time

from StockTickerEngine.StockTickerEngine import StockTickerEngine
from StockTickerHandler import StockTickerHandler

class StockTickerManager(object):
    _logger = None

    def __init__(self, config, logger, handler):
        self._c = config
        self._logger = logger
        self._tickerHandler = handler

    def DisplayQuote(self, tickerSymbol, currentPrice):
        """
            Displays quote to stdout
        """
        divider = "================="

        print (divider)
        print ("Ticker: {} Price: {}".format(tickerSymbol.upper(), currentPrice))
        print (divider + "\n")

    def ProcessQuoteByTicker(self, ticker):
        """
            Processes a quote by calling the ticker handler specified
        """

        if ticker:
            quote = self._tickerHandler.GetStockQuote(ticker)
            currentPrice = quote['l_cur'] if quote else self._c.config["quoteErrMessaage"]
            self.DisplayQuote(ticker, currentPrice)

    def Process(self):
        """
            Processes a list of quotes
        """

        timeDelay = 1

        try:
            tickersList = self._tickerHandler.GetTickerSymbolsFromFile(self._c.config["tickersDataFile"])

            if tickersList:
                for ticker in tickersList:
                    self.ProcessQuoteByTicker(ticker)
                    time.sleep(timeDelay)
            else:
                self._logger.exception("Failed to retrieve stock ticker list.")
        except Exception as err:
            self._logger.exception("Exception: {}".format(str(err)))