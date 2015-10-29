#!/usr/bin/env python
#
# Kenny Kirtland
# @2015
#
# Stock Ticker application
#
#

from StockTickerConfig import StockTickerConfig
from StockTickerEngine.StockTickerEngine import StockTickerEngine
from StockTickerHandler import StockTickerHandler

import time
import logging

c = StockTickerConfig("stockticker.config")
tickerHandler = StockTickerHandler(StockTickerEngine(c.config["url"], c.config["tickersDataFile"]))

def DisplayQuote(tickerSymbol, currentPrice):
    """
        Displays quote to stdout
    """
    divider = "================="

    print (divider)
    print ("Ticker: {} Price: {}").format(tickerSymbol.upper(), currentPrice)	   
    print (divider + "\n")

def ProcessQuoteByTicker(ticker):
    """
        Processes a quote by calling the ticker handler specified
    """

    if ticker:
        quote = tickerHandler.GetStockQuote(ticker)
        currentPrice = quote['l_cur'] if quote else c.config["quoteErrMessaage"]
        DisplayQuote(ticker, currentPrice)

def main():
    """
        Main method to retrieve ticker symbols and process each one
    """
    timeDelay = 1
    loggerName = c.config["loggerName"]
    logFileName = loggerName + ".log"

    logging.basicConfig(filename=logFileName, level=logging.ERROR,)
    log = logging.getLogger(loggerName)
   
    try:        
        tickersList = tickerHandler.GetTickerSymbolsFromFile()

        if tickersList:
            for ticker in tickersList:
                ProcessQuoteByTicker(ticker)
                time.sleep(timeDelay)
        else:
            log.exception("Failed to retrieve stock ticker list.")
    except Exception as err:
        log.exception("Exception: {}".format(str(err)))
        

if __name__ == '__main__':
    main()

