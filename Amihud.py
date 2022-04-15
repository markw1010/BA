import sys

import np as np
import numpy
import matplotlib.pyplot as plt
import pandas as pd

"""
This class provides all necessary methods and variables to calculate the amihud liquidity estimator for a daily, hourly 
or minutely cvs datasets respectively. 

Amihud, Y., 2002. Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets 5. 
31-56
"""


class Amihud:
    numpy.set_printoptions(threshold=sys.maxsize)


    """
    This method returns an array of the open prices of BTC in a specific time period and currency filtered out of a cvs 
    file

    Requires:   the column with the data for the open prices has to be called 'open' in the cvs file
                The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    An Array will be returned with all the open data represented as Strings
    
    Returns:    open - Array with all the open data represented as Strings
    """
    def getOpen(self, file):

        open = file['open'].to_numpy()

        # print(*open, sep='\n')

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
    def getClose(self, file):

        close = file['close'].to_numpy()

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
    def getVolume(self, file, currency):

        volume = file['Volume ' + currency]

        return volume

    """
    This method prints the value for the amihud estimator which is referenced at the top of the class description. 
    Therefore it first extract all relevant data in String format, then the data will be saved as floater so that the 
    value for the amihud estimator can be calculated. At the end, the value will be printed on the console

    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the amihud estimator as well as other pre calculation values will be printed on the 
                console 
    """
    def amihudDetailed(self, file, currency):
        amihud = self.calculateAmihud(file, currency)
        expression = self.getAmihudExpression(file, currency)
        self.printAmihud(amihud, expression)

    """
    This method prints only the value for the amihud estimator on the console.
    
    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the amihud estimator will be printed on the console 
    """

    def amihudValueOnly(self, file, currency):
        amihud = self.calculateAmihud(file, currency)

        print(currency + ' Amihud:')
        print(amihud)

    """
    This method is only implemented for the use of comparison to the CS estimator in the comparison class.
    """

    def amihudComparison(self, file, currency):
        amihud = self.calculateAmihud(file, currency)

        print(currency + ' Amihud:')
        print(amihud)

    """
    this method prints the values for the open and close data as well as the Volume (in USD). it also prints the counter
    values which represent close value divided by the open value -1 for value i. expression will divide value i in 
    counter by value i in the dollar volume. sum represents al the summed up values of expression and amihud is the 
    value of sum divided by the amount of values in expression.

    Ensures:    the values for the open, close, volume USD, counter, expression, sum and the amihud estimator will be 
                printed on the console
    """

    def printAmihud(self, amihud, expression, file, currency):
        print('open')
        print(self.getOpen(file))
        print('----------------')
        print('close')
        print(self.getClose(file))
        print('----------------')
        print('volume USD')
        print(self.getVolume(file, currency))
        print('----------------')
        print('counter')
        print(np.counter)
        print('----------------')
        print('expression')
        print(self.getAmihudExpression(file, currency))
        print('----------------')
        print('len(expression)')
        print(len(self.getAmihudExpression(file, currency)))
        print('----------------')
        print('self.getAmihudSum(expression)')
        print(self.getAmihudSum(expression))
        print('----------------')
        print('amihud')
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

    def calculateAmihud(self, file, currency):
        expression = self.getAmihudExpression(file, currency)
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
    def getAmihudExpression(self, file, currency):
        open = self.getOpen(file)
        close = self.getClose(file)
        volume = self.getVolume(file, currency)

        np.seterr(invalid='ignore')  # This tells NumPy to hide any warning with some “invalid” message in it
        np.counter = [(close / open) - 1 for close, open in zip(close, open)]
        np.counter = np.absolute(np.counter)
        # np.counter = np.divide(np.closeFlt, np.openFlt, out=np.zeros_like(np.closeFlt), where=np.openFlt != 0)
        expression = np.divide(np.counter, volume, out=np.zeros_like(np.counter), where=volume != 0)
        expression = expression[
            ~numpy.isnan(expression)]  # to remove all nan values ( caused by missing USD volume values)

        return expression

    """
    this method takes four arrays which are containing the amihud values in all representative currency pairs and 
    figures out which array contains the fewest data.
    
    Requires:   
    
    Ensures:    An integer value above -1 will be return
    
    Returns:    the amount of data that the smallest array contains
    """
    def getSmallest(self, usd, eur, gbp, jpy):
        usd = len(self.getAmihudExpression(usd, 'USD'))
        eur = len(self.getAmihudExpression(eur, 'EUR'))
        gbp = len(self.getAmihudExpression(gbp, 'GBP'))
        jpy = len(self.getAmihudExpression(jpy, 'JPY'))

        amihudValues = (usd, eur, gbp, jpy)

        smallest = amihudValues.index(min(amihudValues))

        return amihudValues[smallest]

    """
    This method cuts all four arrays to the amount of data that contains the smallest of the four arrays. The arrays 
    are containing the Amihud values and each array represent one currency pair
    
    Requires:
    
    Ensures: four arrays with the exact same amount of data will be returned
    
    Returns:    cuted arrays on the smallest amount of data of each currency pair 
    """
    def cutAhArray(self, usd, eur, gbp, jpy):

        smallestArray = self.getSmallest(usd, eur, gbp, jpy)

        date = usd['date'].to_numpy()
        usd = self.getAmihudExpression(usd, 'USD')
        eur = self.getAmihudExpression(eur, 'EUR')
        gbp = self.getAmihudExpression(gbp, 'GBP')
        jpy = self.getAmihudExpression(jpy, 'JPY')

        date = date[:smallestArray]
        usd = usd[:smallestArray]
        eur = eur[:smallestArray]
        jpy = jpy[:smallestArray]
        gbp = gbp[:smallestArray]

        return date, usd, eur, gbp, jpy

    """
    This method prints the standardised arrays containing the amihud values for each currency pair
    """
    def printStandardisedAh(self, fileUSD, fileEUR, fileGBP, fileJPY):

        date, usd, eur, gbp, jpy = self.cutAhArray(fileUSD, fileEUR, fileGBP, fileJPY)

        ahValues = {
            'Date': date,
            'BTCUSD': usd,
            'BTCEUR': eur,
            'BTCGBP': gbp,
            'BTCJPY': jpy
        }

        dataframe = pd.DataFrame(ahValues)
        dataframe = dataframe.set_index('Date')

        print(dataframe)

