#
# Kenny Kirtland
# @2015
#
# Stock Ticker Handler Tests
#
#

from unittest import TestCase
from unittest.mock import patch

from StockTickerHandler import StockTickerHandler

@patch('StockTickerEngine.StockTickerEngine')
class StockTickerHandlerTest(TestCase):
    def test_GetStockQuote_AssertQuoteNotNone(self, mockedStockTickerEngine):
        tickerSymbol = "TRAK"
        tickerHandler = StockTickerHandler(mockedStockTickerEngine)
        quote = tickerHandler.GetStockQuote(tickerSymbol)
        self.assertIsNotNone(quote)

    def test_GetStockQuote_AssertGetQuoteStockQuoteCalledWithTickerSymbol(self, mockedStockTickerEngine):
        tickerSymbol = "TRAK"
        tickerHandler = StockTickerHandler(mockedStockTickerEngine)
        tickerHandler.GetStockQuote(tickerSymbol)
        mockedStockTickerEngine.GetStockQuote.assert_called_with(tickerSymbol)

    def test_GetStockQuote_AssertGetQuoteGetTickerSymbolsFromFileCalledWithTickerSymbol(self, mockedStockTickerEngine):
        fileName = "test.dat"
        tickerHandler = StockTickerHandler(mockedStockTickerEngine)
        tickerHandler.GetTickerSymbolsFromFile(fileName)
        mockedStockTickerEngine.GetTickerSymbolsFromFile.assert_called()

    def test_GetStockQuote_GetTickerSymbolsFromFile_Returns_5(self, mockedStockTickerEngine):
        expected = 5

        fileName = "test.dat"
        tickerHandler = StockTickerHandler(mockedStockTickerEngine)
        tickerList = tickerHandler.GetTickerSymbolsFromFile(fileName)
        actual = len(tickerList)
        self.assertEquals(actual, expected)

    def test_GetStockQuote_GetTickerSymbolsFromFile_File_Not_Found(self, mockedStockTickerEngine):
        nonExistentFileName = "test_dummy.dat"
        tickerHandler = StockTickerHandler(mockedStockTickerEngine)

        with self.assertRaises(FileNotFoundError):
            tickerHandler.GetTickerSymbolsFromFile(nonExistentFileName)

if __name__ == "__main__":
    main()
