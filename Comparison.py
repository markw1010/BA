import numpy as np

from AbdiRanaldo import AbdiRanaldo
from Amihud import Amihud
from CorwinSchultz import CorwinSchultz
from ExtractData import ExtractData

"""
This class provides variables and methods to make it possible to print both the AH and the CS estimator at the same time
the console for comparison.
"""


class Comparison(ExtractData):

    highStr = []
    lowStr = []

    np.highFlt = []
    np.lowFlt = []

    openStr = []
    closeStr = []
    volumeUSDStr = []

    np.openFlt = []
    np.closeFlt = []
    np.volumeUSDFlt = []

    """
    This method copies the high price, close price, open price, close price, and the USD volume of the arrays into other 
    arrays named np.highFlt, np.lowFlt, np.openFlt, np.closeFlt and np.volumeUSDFlt as floater value.

    Requires:   all the values in highStr, lowStr, openStr, closeStr and volumeUSDStr should contain only floater values

    Ensures:    all values in highStr, lowStr, openStr, closeStr and volumeUSDStr will be copied in separated arrays as 
                floater values
    """

    # TODO make it work for all types of currencies not only USD!
    def extractFlt(self):
        for value in self.highStr:
            np.highFlt.append(float(value))
        for value in self.lowStr:
            np.lowFlt.append(float(value))
        for value in self.openStr:
            np.openFlt.append(float(value))
        for value in self.closeStr:
            np.closeFlt.append(float(value))
        for value in self.volumeUSDStr:
            np.volumeUSDFlt.append(float(value))

    """
    This method extract the high prices and low prices of a cvs file with daily, hourly or minutely data and safes them 
    as strings in separated arrays called highStr and lowStr. 

    Requires:   The cvs file has to be formatted so that it can be read
                The columns in the cvs file have to be called 'high' and 'close' 

    Ensures:    two arrays will be filled with the string representatives of the high price and low price respectively 
    """

    # TODO make it work for all types of currencies not only USD!
    def extractStr(self, fileReader):
        for item in fileReader:
            self.highStr.append(item['high'])
            self.lowStr.append(item['low'])
            self.openStr.append(item['open'])
            self.closeStr.append(item['close'])
            self.volumeUSDStr.append(item['Volume USD'])
        self.highStr.remove('high')
        self.lowStr.remove('low')
        self.openStr.remove('open')
        self.closeStr.remove('close')
        self.volumeUSDStr.remove('Volume USD')

    """
    This method prints the Amihud, the CS and the Abdi and Ranaldo estimator values of a given csv dataset on the 
    console.
    
    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon
    
    Ensures:    Two floater values for the AH and the CS estimator respectively will be printed on the console
    """

    def comparison(self, fileReader):

        cs = CorwinSchultz()
        ah = Amihud()
        ar = AbdiRanaldo()

        self.extractStr(fileReader)
        self.extractFlt()

        cs.corwinSchultzComparison()
        print('-----------')
        ah.amihudComparison()
        print('-----------')
        ar.abdiRanaldoComparison()
