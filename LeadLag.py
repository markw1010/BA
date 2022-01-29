import csv

import numpy as np
import pandas
import matplotlib.pyplot as plt

"""
This class contains methods to calculate the Lead Lag effects of one BTC-currency pair on another
"""
class LeadLag():

    """
    This method calculates the returns of the close values of a cryptocurrency dataset by dividing the close value at
    t+1 by the close value at t and subtract the value by 1
    """
    # TODO close data for returns - Alex?
    def getReturn(self, file):

        close = file['close'].to_numpy()
        closePlusOne = np.delete(np.copy(close), 0)
        modClose = np.delete(np.copy(close), -1)

        np.seterr(invalid='ignore')  # This tells NumPy to hide any warning with some “invalid” message in it
        expression = [closePlusOne / modClose - 1 for closePlusOne, modClose in zip(closePlusOne, modClose)]

        return expression

    """
    This method takes datasets of the currency pairs BTC/USD, BTC/EUR, BTC/JPY and BTC/GBP and prints all the returns
    of each currency pair in one dataframe. The amount of data is limited by the shortest available dataset of the 
    available BTC-currency pair.
    """
    def createDataFrame(self, usdReturns, eurReturns, jpyReturns, gbpReturns):

        returns = { 'time': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[0],
                   'BTC/USD returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[1],
                   'BTC/EUR returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[2],
                   'BTC/JPY returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[3],
                   'BTC/GBP returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[4],
                   }

        df = pandas.DataFrame(returns)

        return df

    """
    This method returns the returns of one BTC- currency pair with the specific timestamp. The length of the dataset 
    is standardise of the smallest dataset of each BTC-currency pair available
    """
    def createDataFrameSingeCurrency(self, usdReturns, eurReturns, jpyReturns, gbpReturns, currency):

        if currency == 'USD':
            returns = {'time': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[0],
                        'BTC/USD returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[1]}
        if currency == 'EUR':
            returns = {'time': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[0],
                        'BTC/EUR returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[2]}
        if currency == 'JPY':
            returns = {'time': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[0],
                        'BTC/JPY returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[3]}
        if currency == 'GBP':
            returns = {'time': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[0],
                        'BTC/GBP returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[4]}

        df = pandas.DataFrame(returns)

        return df

    """
    This method standardise the amount of data points of each BTC-currency pair by identifying the BTC- currency pair 
    with the lowest amount of data and cutting all the other datasets off by the amount of the lowest dataset. E.g. 
    if BTC/USD contains 1000 data points and BTC/EUR only 750, then the BTC/USD dataset will be cut off by 750 data 
    points.
    """
    def standardiseLength(self, usdReturns, eurReturns, jpyReturns, gbpReturns):

        eur, gbp, jpy, usd = self.returns(eurReturns, gbpReturns, jpyReturns, usdReturns)
        returns = np.array([len(usd), len(eur), len(jpy), len(gbp)])
        smallestArray = min(returns)
        eur, gbp, jpy, time, usd = self.standardisedReturns(eur, gbp, jpy, smallestArray, usd, usdReturns)

        return time, usd, eur, jpy, gbp

    """
    This is a helper method of standardiseLength() and it returns the standardised BTC-currency pair returns
    """
    def standardisedReturns(self, eur, gbp, jpy, smallestArray, usd, usdReturns):
        time = usdReturns['date'].to_numpy()[:smallestArray]
        usd = usd[:smallestArray]
        eur = eur[:smallestArray]
        jpy = jpy[:smallestArray]
        gbp = gbp[:smallestArray]
        return eur, gbp, jpy, time, usd

    """
    This is a helper method of standardiseLength() and it returns the un-standardised BTC-currency pair returns
    """
    def returns(self, eurReturns, gbpReturns, jpyReturns, usdReturns):
        usd = self.getReturn(usdReturns)
        eur = self.getReturn(eurReturns)
        jpy = self.getReturn(jpyReturns)
        gbp = self.getReturn(gbpReturns)
        return eur, gbp, jpy, usd


    """
    This method plots all of the BTC-currency pairs in one line diagram
    """
    def plotDf(self, usdReturns, eurReturns, jpyReturns, gbpReturns, currency, currency2, currency3, currency4):

        df = self.createDataFrame(usdReturns, eurReturns, jpyReturns, gbpReturns)
        plt.title('returns')
        plt.plot(df['time'], df['BTC/' + currency + ' returns'], df['time'], df['BTC/' + currency2 + ' returns'],
                 df['BTC/' + currency3 + ' returns'], df['BTC/' + currency4 + ' returns'])
        plt.xlabel('time')
        plt.ylabel('return')
        plt.show()

    #def plotOne(self, ):
