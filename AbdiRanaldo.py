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
    def arGraph(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        dataframe = self.getNormalizedDataframe(fileEUR, fileGBP, fileJPY, fileUSD, int)
        dataframe = self.setDateIndex(dataframe)
        self.pltShow(dataframe, int)

    """
    This method sets the index of a given dataframe to the date column of the dataframe. Therefore the date values have 
    to transferred to integer values first.

    Requires:       The given dataframe has to have one column with date values
                    the dataframe has to store at least one row of values

    Ensures:        a dataframe will be returned 

    Returns:        a dataframe with Date values as index
    """

    def setDateIndex(self, dataframe):
        dataframe = pd.DataFrame(dataframe)
        dataframe['Date'] = dataframe['Date'].astype('datetime64')  # to set date as integer values
        dataframe = dataframe.set_index('Date')
        return dataframe

    """
    This method helps to get a dataframe of Amihud values of one currency pair, depending on the int value that is 
    given. Therefore the Amihud values of each currency pair has to be standardised on the same length. Following int 
    values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def getNormalizedDataframe(self, fileEUR, fileGBP, fileJPY, fileUSD, int):
        date, usd, eur, gbp, jpy = self.cutArArray(fileUSD, fileEUR, fileGBP, fileJPY)
        dataframe = self.chooseCurrencyPair(date, eur, gbp, int, jpy, usd)
        return dataframe

    """
    In this method are all the settings defined to plot a dataframe with some kind of numerical values on y-axis and 
    date values on the x-axis. Following int values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def pltShow(self, dataframe, int):
        plt.xlabel('Date')
        plt.ylabel('Values')
        self.chooseTitle(int)
        plt.plot(dataframe)
        plt.show()

    """
    This method plots the autocorrelation of the amihud values in a graph
    """
    def showAutocorrGraph(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        self.calcAutocorrGraph(fileEUR, fileGBP, fileJPY, fileUSD, int)

        plt.show()

    """
    This method calculates the autocorrelation of of past BTC liquidity data for each BTC currency pair. Date values are 
    the index. Following int values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def calcAutocorrGraph(self, fileEUR, fileGBP, fileJPY, fileUSD, int):
        ahValues = self.getNormalizedDataframe(fileEUR, fileGBP, fileJPY, fileUSD, int)
        dataframe = pd.DataFrame(ahValues)
        dataframe['Date'] = dataframe['Date'].astype('datetime64')  # to set date as integer values
        dataframe = dataframe.set_index('Date')
        autocorrelation_plot(dataframe)
        self.chooseTitle(int)

    """
    This is a helper method to set a title for autocorrelation graph of the autocorrGraph method, depending on what 
    currency should be shown. 0 refers to USD, 1 refers to EUR, 2 refers GBP and 3 refers to JPY
    """
    def chooseTitle(self, int):
        if int == 0:
            plt.title('Abdi and Ranaldo measure USD')
        if int == 1:
            plt.title('Abdi and Ranaldo measure EUR')
        if int == 2:
            plt.title('Abdi and Ranaldo measure GBP')
        if int == 3:
            plt.title('Abdi and Ranaldo measure JPY')

    """
    This is a helper method to for the autocorrGraph method to choose a currency pair. 0 refers to USD, 1 refers to EUR, 
    2 refers GBP and 3 refers to JPY
    """
    def chooseCurrencyPair(self, date, eur, gbp, int, jpy, usd):
        if int == 0:
            arValues = {
                'Date': date,
                'BTCUSD': usd,
            }
        if int == 1:
            arValues = {
                'Date': date,
                'BTCEUR': eur,
            }
        if int == 2:
            arValues = {
                'Date': date,
                'BTCGBP': gbp,
            }
        if int == 3:
            arValues = {
                'Date': date,
                'BTCJPY': jpy,
            }
        return arValues