import numpy as np

from AbdiRanaldo import AbdiRanaldo
from Amihud import Amihud
from CorwinSchultz import CorwinSchultz

"""
This class provides variables and methods to make it possible to print both the AH and the CS estimator at the same time
the console for comparison.
"""


class Comparison():

    highStr = []
    lowStr = []


    """
    This method prints the Amihud, the CS and the Abdi and Ranaldo estimator values of a given csv dataset on the 
    console.
    
    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon
    
    Ensures:    Two floater values for the AH and the CS estimator respectively will be printed on the console
    """

    def comparison(self, file, currency):

        cs = CorwinSchultz()
        ah = Amihud()
        ar = AbdiRanaldo()

        cs.corwinSchultzComparison(file, currency)
        print('-----------')
        ah.amihudComparison(file, currency)
        print('-----------')
        ar.abdiRanaldoComparison(file, currency)
        print(' ')
        print(' ')
