#!/usr/bin/env python
#
# Kenny Kirtland
# @2015
#
# Stock Ticker application
#
#

import logging

from StockTickerManager import StockTickerManager
from StockTickerConfig import StockTickerConfig
from StockTickerHandler import StockTickerHandler
from StockTickerEngine import StockTickerEngine

def GetLogger(loggerName):
    """
        Creates logger
    """

    logFileName = loggerName + ".log"
    logger = logging.basicConfig(filename=logFileName, level=logging.ERROR,)
    log = logging.getLogger(loggerName)

    return log

def main():
    """
        Main method to retrieve ticker symbols and process each one
    """
    configFile = "stockticker.config"
    c = StockTickerConfig(configFile)
    url = c.config["url"]
    stockTickerEngine = StockTickerEngine.StockTickerEngine(url)
    loggerName = c.config["loggerName"]
    logger = GetLogger(loggerName)
    handler = StockTickerHandler(stockTickerEngine)
    manager = StockTickerManager(c, logger, handler)
    manager.Process()

if __name__ == '__main__':
    main()

