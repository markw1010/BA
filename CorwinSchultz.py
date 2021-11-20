import math

import numpy
import numpy as np
from numpy.ma import indices

"""
This class provides all necessary methods and variables to calculate the amihud liquidity estimator for a daily, hourly
or minutely datasets respectively.
"""
class CorwinSchultz:

    highStr = []
    lowStr = []

    np.highFlt = []
    np.lowFlt = []

    np.arr = []

    """
    This method prints the value for the amihud estimator which is referenced at the top of the class description. 
    Therefore it first extract all relevant data in String format, then the data will be saved as floater so that the 
    value for the amihud estimator can be calculated. At the end, the value will be printed on the console

    Requires:   The cvs file has to be formatted so that it can be readed
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the amihud estimator will be returned 
    """
    def corwinSchultz(self, fileReader):

        self.extractStr(fileReader)

        self.extractFlt()

        #self.getBeta()

        self.getGamma()

        #print(np.highFlt)
        #print(self.highDivLow())

        #self.printCS()


    """
    this method calculates the value for the amihud estimator and returns it. Therefore it refers to the calculation of 
    the counter part of the estimator as well as the sum value. The value of the amihud estimator is the sum divided by 
    the number of data for open, close an volume.

    Requires:   expression should at least contain one element

    Ensures:    the value for the amihud estimator will be returned
    """
    def calculateCS(self):
        # self.getAlphsCS()

        self.getBeta()

        # self.getGammaCS()

    """
    This method returns an array of the values for the counter part of the amihud estimator which is the quotient of the 
    closing price in subinterval i of interval t and opening price in subinterval i of interval t in a specific time 
    period subtracted by one and divided by the dollar volume (or the volume in any other currency). This term is called 
    'expression' After all the values are calculated, the data which is nan will be replaced by 0. nan values occur if 
    there is no valid data for the volume so it is represented as 0 in the cvs document and the counter part divided by 
    0 is not defined).

    Requires:   np.openFlt shouldn't contain a 0 item
                np.closeFLt and np.openFlt and np.volumeUSDFlt should contain the same amount of items

    Ensures:    an array will be returned containing the expression values
    
    Returns: 
    """
    # TODO Exception handling if item in open is 0!
    def getBeta(self):

        highDivLow = self.highDivLow()

        ln = numpy.log(highDivLow)

        firstTerm = numpy.power(ln, 2)

        secondTerm = np.delete(np.copy(firstTerm),0) #fitsTerm w/o first element

        beta = [x + y for x, y in zip(firstTerm, secondTerm)]

        return beta


    """
    this method takes an array and makes two arrays of it while in the array called arri1 the first element is removed 
    and on the arrModified array the last element is removed. Then both arrays are compared element wise and the the 
    bigger item will be put into the max array
    
    Requires:   The input Array has to contain numbers only  
                The input Array has to have at least 2 Items 
                
    Ensures:    max contains at least two elements 
    
    Returns:    max - Array which contains the maximum of the shifted compared input array
    """
    def getMaxPrice(self, arr):

        arrModified = np.delete(arr, -1)   # -1 is the index for the last item in an array
        arri1 = np.delete(arr, 0)

        max = np.maximum(arrModified, arri1)

        return max


    # TODO Error handling if div by 0!
    def getGamma(self):

        hii1 = self.getMaxPrice(np.highFlt)

        lii1 = self.getMaxPrice(np.lowFlt)

        gamma = self.calcGamma(hii1, lii1)

        return gamma


    """
    This method takes two arrays hii1 and lii1 and divide the values element wise. After the natural logarithm of each 
    item will be calculated and be set to the power of two. We call the array that includes all the results gamma
    
    Requires:   Both input arrays should have the same amount of items
                All items in teh hii1 and lii1 array should only contain numbers > 0
                
    Ensures:    gamma only contains numbers > 0
    
    Returns:    gamma - Array which contains all the values after the calculations described above
    """
    def calcGamma(self, hii1, lii1):
        highDivLow = [high / low for high, low in zip(hii1, lii1)]
        ln = numpy.log(highDivLow)
        gamma = numpy.power(ln, 2)
        return gamma

    def highDivLow(self):
        np.seterr(invalid='ignore')  # This tells NumPy to hide any warning with some “invalid” message in it
        highDivLow = np.divide(np.highFlt, np.lowFlt, out=np.zeros_like(np.highFlt), where=np.lowFlt != 0)
        highDivLow = highDivLow[
            ~numpy.isnan(highDivLow)]  # to remove all nan values (caused by missing low prices)
        return highDivLow

    """
    this method prints the values for the open and close data as well as the Volume (in USD). it also prints the counter
    values which represent close value divided by the open value -1 for value i. expression will divide value i in 
    counter by value i in the dollar volume. sum represents al the summed up values of expression and amihud is the 
    value of sum divided by the amount of values in expression.

    Ensures:    the values for the open, close, volume USD, counter, expression, sum and the amihud estimator will be 
                printed on the console
    """
    def printCS(self):
          # print('high')
          # print(np.highFlt)
          print('----------------')
          # print('low')
          # print(np.lowFlt)
          # print('----------------')
          # print('len(low)')
          # print(len(np.lowFlt))
          # print('----------------')
          # print('len(high)')
          # print(len(np.highFlt))
          # print('----------------')
          # print('beta')
          # print(self.getBetaCS())
          # print('----------------')
          # print('highDivLow')
          # print(self.highDivLow())
          # print('----------------')
          # print('len(self.highDivLow())')
          # print(len(self.highDivLow()))
          # print('--------------')
          print('self.getBetaCS()')
          print(self.getBeta())
          # print('--------------')
          # print(*self.getBetaCS(), sep='\n')
          print('len(np.betaOne)')
          print(len(self.getBeta()))
          # print('--------------')


    """
    This method returns an array with the close prices of BTC in a specific time period

    Requires:   the column with the data for the close prices has to be called 'close' in the cvs file
                The cvs file has to be formatted so that it can be readed
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    An Array will be returned with all the close data represented as Strings
    
    Returns: 
    """
    def getHighCS(self, fileReader):
        high = []

        for item in fileReader:
            high.append(item['high'])

        # print(*values, sep='\n')
        print(high)

        return high


    """
    This method returns an array with the close prices of BTC in a specific time period

    Requires:   The cvs file has to be formatted so that it can be read
                the column with the data for the close prices has to be called 'close' in the cvs file                    
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    An Array will be returned with all the close data represented as Strings
        
    Returns:    
    """
    def getLowCS(self, fileReader):
        low = []

        for item in fileReader:
            low.append(item['low'])

        # print(*values, sep='\n')
        print(low)

        return low


    """
    This method takes the open price, close prise and volume USD amount of the arrays and copies them into arrays which 
    are saving the values as floater

    Requires:   all the values in openStr, closeStr and volumeUSDStr should contain only floater values 

    Ensures:    all values in openStr, closeStr and volumeUSDStr will be copied in separated arrays as floater values 
    """

    # TODO make it work for all types of currencies not only USD!
    def extractFlt(self):
        for value in self.highStr:
            np.highFlt.append(float(value))
        for value in self.lowStr:
            np.lowFlt.append(float(value))


    """
    This method extract the open prices, close prices and USD volume of a cvs file with daily, hourly or minutely data 
    and safes them as Strings an separated arrays. 

    Requires:   The cvs file has to be formatted so that it can be readed
                The columns in the cvs file have to be called 'open', 'close' and 'VolumeUSD'

    Ensures:    three arrays will be filled with the string values of the open price, close price and VolumeUSD 
                respectively 
    """
    # TODO make it work for all types of currencies not only USD!
    def extractStr(self, fileReader):
        for item in fileReader:
            self.highStr.append(item['high'])
            self.lowStr.append(item['low'])
        self.highStr.remove('high')
        self.lowStr.remove('low')