import sys
from datetime import datetime

import np as np
import numpy
from tabulate import tabulate

"""
This class provides all necessary methods and variables to calculate the amihud liquidity estimator for a daily, hourly 
or minutely cvs datasets respectively. 

Amihud, Y., 2002. Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets 5. 
31-56
"""
class Amihud:
    numpy.set_printoptions(threshold=sys.maxsize)

    openStr = []
    closeStr = []
    volumeUSDStr = []

    np.openFlt = []
    np.closeFlt = []
    np.volumeUSDFlt = []

    """
    this method standardise the unix time stamp. In case that the unix code in the cvs file has parts of the data in 
    second format and other parts in millisecond format, this method will standardise the timestamp. Therefore it 
    checks, if the amount of characters of the time stamp is above or under 10. If it is above 10, the code is in 
    milliseconds, otherwise it will be in seconds

    Requires:   the name of the column with the unix time stamp in the cvs file has to be called 'unix'
                the unix data has to be in seconds or in milliseconds

    Ensures:    The right date and time will be returned in the format: yyyy-mm-dd hh:mm:ss
    
    Returns:    time - The right date and time in the format: yyyy-mm-dd hh:mm:ss
    """
    def standardiseUnix(self, item):
        unixMilliseconds = int(item.get('unix')) / 1000
        unixSeconds = int(item.get('unix'))
        if (len(item['unix']) <= 10):
            time = datetime.utcfromtimestamp(unixSeconds).strftime('%Y-%m-%d %H:%M:%S')
        else:
            time = datetime.utcfromtimestamp(unixMilliseconds).strftime('%Y-%m-%d %H:%M:%S')
        return time

    """
    This method returns an array of the open prices of BTC in a specific time period and currency filtered out of a cvs 
    file

    Requires:   the column with the data for the open prices has to be called 'open' in the cvs file
                The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    An Array will be returned with all the open data represented as Strings
    
    Returns:    open - Array with all the open data represented as Strings
    """

    def getOpen(self, fileReader):

        open = []

        for item in fileReader:
            open.append(item['open'])

        # print(*values, sep='\n')
        print(open)

        return open

    """
    This method returns an array with the close prices of BTC in a specific time period and currency filtered out of a 
    cvs file

    Requires:   the column with the data for the close prices has to be called 'close' in the cvs file
                The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    An Array will be returned with all the close data represented as Strings
    
    Returns:    open - Array with all the close data represented as Strings
    """
    def getClose(self, fileReader):

        close = []

        for item in fileReader:
            close.append(item['close'])

        # print(*values, sep='\n')
        print(close)

        return close

    """
    This method returns an array with the volume data of BTC traded in different currencies in a specific time period
    and currency filtered out of a cvs file

    Requires:   the column with the data for the volume has to be called 'Volume[currency short e.g. USD]'  in the cvs 
                file
                The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon
                Depending on the data set a valid currency has to be given by the argument. 

    Ensures:    An Array will be returned with all the volume data represented as Strings
    
    Returns:    volume - Array with all the volume data represented as Strings
    """
    def getVolume(self, fileReader, currency):

        volume = []

        for item in fileReader:
            volume.append(item['Volume' + currency])

        # print(*values, sep='\n')
        print(volume)

        return volume

    """
    This method prints the value for the amihud estimator which is referenced at the top of the class description. 
    Therefore it first extract all relevant data in String format, then the data will be saved as floater so that the 
    value for the amihud estimator can be calculated. At the end, the value will be printed on the console

    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the amihud estimator will be printed on the console 
    """
    def amihud(self, fileReader):

        self.extractStr(fileReader)

        self.extractFlt()

        amihud = self.calculateAmihud()

        expression = self.getAmihudExpression()

        self.printAmihud(amihud, expression)

    """
    this method prints the values for the open and close data as well as the Volume (in USD). it also prints the counter
    values which represent close value divided by the open value -1 for value i. expression will divide value i in 
    counter by value i in the dollar volume. sum represents al the summed up values of expression and amihud is the 
    value of sum divided by the amount of values in expression.

    Ensures:    the values for the open, close, volume USD, counter, expression, sum and the amihud estimator will be 
                printed on the console
    """

    def printAmihud(self, amihud, expression):
        print('open')
        print(np.openFlt)
        print('----------------')
        print('close')
        print(np.closeFlt)
        print('----------------')
        print('volume USD')
        print(np.volumeUSDFlt)
        print('----------------')
        print('counter')
        print(np.counter)
        print('----------------')
        print('expression')
        print(self.getAmihudExpression())
        print('----------------')
        print(self.getAmihudSum(expression))
        print('----------------')
        print(amihud)
        print('----------------')

    """
    this method calculates the value for the amihud estimator and returns it. Therefore it refers to the calculation of 
    the counter part of the estimator as well as the sum value. The value of the amihud estimator is the sum divided by 
    the number of data for open, close an volume.

    Requires:   expression should at least contain one element

    Ensures:    amihud is a single floater
    
    Returns:    amihud - Floater which contains amihud value
    """
    def calculateAmihud(self):
        expression = self.getAmihudExpression()
        sum = self.getAmihudSum(expression)
        amihud = sum / len(expression)
        return amihud

    """
    This method calculates the sum of of all quotients of the closing price in subinterval i of interval t and opening 
    price in subinterval i of interval t in a specific time period subtracted by one and divided by the dollar 
    volume in subinterval i of interval t (or the value in any other currency)

    Requires:   expression should at least contain one element otherwise 0 will be returned

    Ensures:    sum is a single floater
    
    Returns:    sum - Array of all summed up values in the expression array
    """
    def getAmihudSum(self, expression):
        sum = 0
        for i in range(0, len(expression)):
            sum += expression[i]
        return sum

    """
    This method returns an array of the values for the counter part of the amihud estimator which is the quotient of the 
    closing price in subinterval i of interval t and opening price in subinterval i of interval t in a specific time 
    period subtracted by one and divided by the dollar volume (or the volume in any other currency). This term is called 
    'expression' After all the values are calculated, the data which is nan will be replaced by 0. nan values occur if 
    there is no valid data for the volume so it is represented as 0 in the cvs document and the counter part divided by 
    0 is not defined).

    Requires:   np.openFlt shouldn't contain a 0 item
                np.closeFLt and np.openFlt and np.volumeUSDFlt should contain the same amount of items

    Ensures:    expression only contains numerical elements
    
    Returns:    expression - Array which contains the expression values
    """
    # TODO Exception handling if item in open is 0!
    def getAmihudExpression(self):
        np.seterr(invalid='ignore')  # This tells NumPy to hide any warning with some “invalid” message in it
        np.counter = [(close / open) - 1 for close, open in zip(np.closeFlt, np.openFlt)]
        # np.counter = np.divide(np.closeFlt, np.openFlt, out=np.zeros_like(np.closeFlt), where=np.openFlt != 0)
        expression = np.divide(np.counter, np.volumeUSDFlt, out=np.zeros_like(np.counter), where=np.volumeUSDFlt != 0)
        expression = expression[
            ~numpy.isnan(expression)]  # to remove all nan values ( caused by missing USD volume values)
        return expression

    """
    This method copies the open price, close prise and volume USD amount of the arrays into arrays named np.openFlt, 
    np.closeFlt and np.volumeUSDFlt as floater value

    Requires:   all the values in openStr, closeStr and volumeUSDStr should contain only floater values 

    Ensures:    all values in openStr, closeStr and volumeUSDStr will be copied in separated arrays as floater values
    """

    # TODO make it work for all types of currencies not only USD!
    def extractFlt(self):
        for value in self.openStr:
            np.openFlt.append(float(value))
        for value in self.closeStr:
            np.closeFlt.append(float(value))
        for value in self.volumeUSDStr:
            np.volumeUSDFlt.append(float(value))

    """
    This method extract the open prices, close prices and USD volume of a cvs file with daily, hourly or minutely data 
    and safes them as strings in separated arrays called openStr, closeStr and volumeUSDStr. 

    Requires:   The cvs file has to be formatted so that it can be read
                The columns in the cvs file have to be called 'open', 'close' and 'VolumeUSD'

    Ensures:    three arrays will be filled with the string representatives of the open price, close price and VolumeUSD 
                respectively 
    """

    # TODO make it work for all types of currencies not only USD!
    def extractStr(self, fileReader):
        for item in fileReader:
            self.openStr.append(item['open'])
            self.closeStr.append(item['close'])
            self.volumeUSDStr.append(item['VolumeUSD'])
        self.openStr.remove('open')
        self.closeStr.remove('close')
        self.volumeUSDStr.remove('VolumeUSD')


