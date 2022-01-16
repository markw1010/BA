import csv

import numpy as np
import pandas
import matplotlib.pyplot as plt


class LeadLag():

    # TODO close data for returns - Alex?
    def getReturn(self, file):

        close = file['close'].to_numpy()
        closePlusOne = np.delete(np.copy(close), 0)
        modClose = np.delete(np.copy(close), -1)

        np.seterr(invalid='ignore')  # This tells NumPy to hide any warning with some “invalid” message in it
        expression = [closePlusOne / modClose - 1 for closePlusOne, modClose in zip(closePlusOne, modClose)]

        return expression



    def createDataFrame(self, usdReturns, eurReturns, jpyReturns, gbpReturns):

        returns = { 'time': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[0],
                   'BTC/USD returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[1],
                   'BTC/EUR returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[2],
                   'BTC/JPY returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[3],
                   'BTC/GBP returns': self.standardiseLength(usdReturns, eurReturns, jpyReturns, gbpReturns)[4],
                   }

        df = pandas.DataFrame(returns)

        return df

    def printFullReturns(self, usdReturns, eurReturns, jpyReturns, gbpReturns):
        pandas.set_option("display.max_rows", None, "display.max_columns", None)
        df = self.createDataFrame(usdReturns, eurReturns, jpyReturns, gbpReturns).apply(lambda x: x * 100)
        print(df)


    def printFullPercentageReturns(self, usdReturns, eurReturns, jpyReturns, gbpReturns):
        pandas.set_option("display.max_rows", None, "display.max_columns", None)
        print(self.createDataFrame(usdReturns, eurReturns, jpyReturns, gbpReturns))


    def printReturns(self, usdReturns, eurReturns, jpyReturns, gbpReturns):
        print(self.createDataFrame(usdReturns, eurReturns, jpyReturns, gbpReturns))

    def printPercentageReturns(self, usdReturns, eurReturns, jpyReturns, gbpReturns):
        df = self.createDataFrame(usdReturns, eurReturns, jpyReturns, gbpReturns).apply(lambda x: x * 100)
        print(df)


    def standardiseLength(self, usdReturns, eurReturns, jpyReturns, gbpReturns):

        time = usdReturns['date'].to_numpy()
        usd = self.getReturn(usdReturns)
        eur = self.getReturn(eurReturns)
        jpy = self.getReturn(jpyReturns)
        gbp = self.getReturn(gbpReturns)

        returns = np.array([len(usd), len(eur), len(jpy), len(gbp)])

        smallestArray = min(returns)

        time = usdReturns['date'].to_numpy()[:smallestArray]
        usd = usd[:smallestArray]
        eur = eur[:smallestArray]
        jpy = jpy[:smallestArray]
        gbp = gbp[:smallestArray]

        return time, usd, eur, jpy, gbp

    def plotDf(self, usdReturns, eurReturns, jpyReturns, gbpReturns, currency):

        df = self.createDataFrame(usdReturns, eurReturns, jpyReturns, gbpReturns)
        plt.title('BTC/' + currency + ' returns')
        plt.plot(df['time'], df['BTC/' + currency + ' returns'])
        plt.xlabel('time')
        plt.ylabel('return')
        plt.show()
