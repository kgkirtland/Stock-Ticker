#
# Kenny Kirtland
# @2015
#
# Stock Ticker Manager Tests
#
#

from unittest import TestCase
from unittest.mock import patch, MagicMock

from StockTickerConfig import  StockTickerConfig
from StockTickerManager import StockTickerManager

@patch('StockTickerHandler.StockTickerHandler')
@patch('StockTickerManager.StockTickerManager._logger')
class StockTickerManagerTest(TestCase):
    _config = StockTickerConfig("stocktickertest.config")

    def test_Process_Verify_ManagerCreated(self, mockedLogger, mockedHandler):
        manager = StockTickerManager(self._config, mockedLogger, mockedHandler)
        manager.Process()
        self.assertIsNotNone(manager)

    def test_Process_Verify_ProcessQuote_Called(self, mockedLogger, mockedHandler):
        manager = StockTickerManager(self._config, mockedLogger, mockedHandler)
        manager.Process()
        mockedHandler.GetStockQuote.assert_called()

    def test_Process_Verify_ListNotLoaded_ProcessQuote_Not_Called(self, mockedLogger, mockedHandler):
        manager = StockTickerManager(self._config, mockedLogger, mockedHandler)
        mockedHandler.GetTickerSymbolsFromFile = MagicMock(return_value=None)
        manager.Process()
        mockedHandler.GetStockQuote.assert_not_called()

    def test_Process_Verify_ListNotLoaded_Logger_Exception_Called(self, mockedLogger, mockedHandler):
        manager = StockTickerManager(self._config, mockedLogger, mockedHandler)
        mockedHandler.GetTickerSymbolsFromFile = MagicMock()
        mockedHandler.GetTickerSymbolsFromFile.return_value = 8
        manager.Process()
        self.assertEquals(len(mockedLogger.exception.mock_calls), 1)

    def test_Process_Verify_Ticker_TRAK_GetStockQuote_Called(self, mockedLogger, mockedHandler):
        ticker = "TRAK"

        manager = StockTickerManager(self._config, mockedLogger, mockedHandler)
        manager.ProcessQuoteByTicker(ticker)
        mockedHandler.GetStockQuote.assert_called_with(ticker)


    def test_Process_Verify_Ticker_None_GetStockQuote_Not_Called(self, mockedLogger, mockedHandler):
        ticker = None

        manager = StockTickerManager(self._config, mockedLogger, mockedHandler)
        manager.ProcessQuoteByTicker(ticker)
        mockedHandler.GetStockQuote(ticker).assert_not_called()