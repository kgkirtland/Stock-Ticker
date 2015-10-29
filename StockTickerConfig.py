#
# Kenny Kirtland
# @2015
#
# Configuration settings class
#
#

import json

class StockTickerConfig(object):
    """
        This class retrieves the configuration settings from the config file
    """
    def __init__(self, configFile):
        file = open(configFile, 'r').read()
        self.config = json.loads(file)