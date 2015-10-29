#
# Kenny Kirtland
# @2015
#
# Stock Ticker Engine used to retrieve stock quotes from the internets
#
#

import requests
import json

from StockTickerEngine.StockTickerEngineBase import StockTickerEngineBase

class StockTickerEngine(StockTickerEngineBase):
    """
    This class provides a set of methods to retrieve stock quotes from the internets
    """

    def __init__(self, url):
        self.__url = url

    def GetStockQuote(self, tickerSymbol):
        """
            Gets the stock quote by ticker symbol using the url provided in the constructor
        """

        try:
            url = self.__url % str(tickerSymbol)
            response = requests.get(url)
        except requests.exceptions.Timeout as timeoutErr:
            raise requests.exceptions.RequestException(str(timeoutErr))
        except requests.exceptions.RequestException as requestErr:
            raise requests.exceptions.RequestException(str(requestErr))

        if response.status_code != requests.codes.ok:
            raise requests.exceptions.RequestException("Status Code: " + response.status_code)
            return

        lines = response.text.splitlines()
        jsonFormattedResponse = json.loads(''.join([x for x in lines if x not in ('// [', ']')]))

        return jsonFormattedResponse
