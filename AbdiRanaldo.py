import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

"""
This class provides all necessary methods and variables to calculate the AR liquidity estimator for a daily, hourly 
or minutely cvs datasets respectively. 

Abdi, F., Ranaldo, A., 2017. A simple estimation of bid-ask spreads from daily close, high, and low prices. The Review 
of Financial Studies, Volume 30, Issue 12, December 2017. 4437-4480
"""


class AbdiRanaldo:

    """
    This method prints the value for the AR estimator which is referenced at the top of the class description. 
    Therefore it first extract all relevant data in String format, then the data will be saved as floater so that the 
    value for the amihud estimator can be calculated. At the end, the value will be printed on the console

    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the AR estimator as well as other pre calculation values will be printed on the 
                console 
    """

    def printAbdiRanaldo(self, file, currency):
        ARt = self.getARt(file)
        ARi = self.getARi(file)
        print(currency + 'ARi: ')
        print(ARi)
        print('--------------')
        print('len(ARi): ')
        print(len(ARi))
        print('--------------')
        print('np.sum(ARi): ')
        print(np.sum(ARi))
        print('--------------')
        print(currency + 'ARt: ')
        print(ARt)
        print('--------------')

    """
    This method prints only the value for the AR estimator on the console.

    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the AR estimator will be printed on the console 
    """
    def abdiRanaldoValueOnly(self, file, currency):
        ARt = self.getARt(file)

        print(currency + ' ARt: ')
        print(ARt)

    """
    This method is only implemented for the use of comparison to the AR estimator in the comparison class.
    """
    def abdiRanaldoComparison(self, file, currency):
        ARt = self.getARt(file)

        print(currency + ' ARt: ')
        print(ARt)

    def getHi(self, file):
        high = file['high'].to_numpy()
        hi = np.log(high)
        return hi

    def getLi(self, file):
        low = file['low'].to_numpy()
        li = np.log(low)
        return li

    def getCi(self, file):
        close = file['close'].to_numpy()
        ci = np.log(close)
        return ci

    """
    this method returns the value for p_i which ist the addition of hi and li divided by two.
.    
    Requires:   len(hi) = len(li)
    
    Ensures: An array with the pi values will be returned   
    """
    def getPi(self, file):
        hi = self.getHi(file)
        li = self.getLi(file)
        hili = np.add(hi, li)
        pi = np.divide(hili, 2)
        return pi

    """
    This method returns the value of ARi.
    
    Requires:   len(pi1) + len(ci1) >= 4
                term3 >= 0
    
    Ensures:    An array with all ARi values will be returned 
    """
    def getARi(self, file):
        ci = self.getCi(file)
        pi = self.getPi(file)

        pi1 = np.delete(pi, 0)
        ci1 = np.delete(ci, -1)

        firstPart = np.subtract(ci, pi)
        firstPart = np.delete(firstPart, -1)
        secondPart = np.subtract(ci1, pi1)

        term = np.multiply(firstPart, secondPart)
        term2 = np.multiply(term, 4)
        term3 = np.maximum(term2, 0)

        ARi = np.power(term3, 0.5)

        return ARi

    """
    This method calculates and returns the AR_t estimator for interval t which is the average of the AR_t,i measures
    for all adjacent subintervals i in t
    
    Requires:   len(ARi) > 0
    
    Ensures:    A floater value will be returned      
    """
    def getARt(self, file):
        ARi = self.getARi(file)
        sum = np.sum(ARi)
        amount = len(ARi)
        ARt = sum/amount
        return ARt

    """
    this method takes four arrays which are containing the amihud values in all representative currency pairs and 
    figures out which array contains the fewest data.

    Requires:   

    Ensures:    An integer value above -1 will be return

    Returns:    the amount of data that the smallest array contains
    """
    def getSmallest(self, usd, eur, gbp, jpy):
        usd = len(self.getARi(usd))
        eur = len(self.getARi(eur))
        gbp = len(self.getARi(gbp))
        jpy = len(self.getARi(jpy))

        arValues = (usd, eur, gbp, jpy)

        smallest = arValues.index(min(arValues))

        return arValues[smallest]

    """
    This method cuts all four arrays to the amount of data that contains the smallest of the four arrays. The arrays 
    are containing the AR values and each array represent one currency pair

    Requires:

    Ensures:    four arrays with the exact same amount of data will be returned

    Returns:    cuttet arrays on the smallest amount of data of each currency pair 
    """
    def cutArArray(self, usd, eur, gbp, jpy):

        smallestArray = self.getSmallest(usd, eur, gbp, jpy)

        date = usd['date'].to_numpy()
        usd = self.getARi(usd)
        eur = self.getARi(eur)
        gbp = self.getARi(gbp)
        jpy = self.getARi(jpy)

        date = date[:smallestArray]
        usd = usd[:smallestArray]
        eur = eur[:smallestArray]
        jpy = jpy[:smallestArray]
        gbp = gbp[:smallestArray]

        return date, usd, eur, gbp, jpy

    """
    This method prints the standardised arrays containing the amihud values for each currency pair
    
    Returns    pandas dataframe containing AR values for each currency pair and date as int
    """
    def printStandardisedAr(self, fileUSD, fileEUR, fileGBP, fileJPY):

        date, usd, eur, gbp, jpy = self.cutArArray(fileUSD, fileEUR, fileGBP, fileJPY)

        arValues = {
            'Date': date,
            'BTCUSD': usd,
            'BTCEUR': eur,
            'BTCGBP': gbp,
            'BTCJPY': jpy
        }

        dataframe = pd.DataFrame(arValues)
        dataframe['Date'] = dataframe['Date'].astype('datetime64')  # to set date as integer values
        dataframe = dataframe.set_index('Date')

        print(dataframe)
        return dataframe


    """
    This method plots all the CS values in one graph with the date oin the x-axis and the value on the y-axis
    """
    def arGraph(self, fileUSD, fileEUR, fileGBP, fileJPY):

        dataframe = self.printStandardisedAr(fileUSD, fileEUR, fileGBP, fileJPY)

        plt.xlabel('Date')
        plt.ylabel('Values')
        plt.title('CS values')
        plt.plot(dataframe)

        plt.show()

    """
    This method plots the autocorrelation of the amihud values in a graph
    """

    def autocorrGraph(self, fileUSD, fileEUR, fileGBP, fileJPY):
        dataframe = self.printStandardisedAr(fileUSD, fileEUR, fileGBP, fileJPY)

        autocorrelation_plot(dataframe)

        plt.show()