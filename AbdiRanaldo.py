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
    def getStandardisedAr(self, fileUSD, fileEUR, fileGBP, fileJPY):

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

        #print(dataframe)
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

    """
    This method defines the leading and the lagging variable and calculates the cross correlation with a lag up to 24.
    The lag up to 24 is chosen, bc the main use of this program is to work with hourly data and bc BTC is traded 24/7,
    the maximum lag of 24 is representing one day. The date values are the index. Following int values allow access to 
    following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def defineLeaderLagger(self,usd, eur, gbp, jpy, leader, lagger):
        if leader == 0 and lagger == 1:
            xcov = usd.corr(eur)
        if leader == 0 and lagger == 2:
            xcov = usd.corr(gbp)
        if leader == 0 and lagger == 3:
            xcov = usd.corr(jpy)
        if leader == 1 and lagger == 0:
            xcov = eur.corr(usd)
        if leader == 1 and lagger == 2:
            xcov = eur.corr(gbp)
        if leader == 1 and lagger == 3:
            xcov = eur.corr(jpy)
        if leader == 2 and lagger == 0:
            xcov = gbp.corr(usd)
        if leader == 2 and lagger == 1:
            xcov = gbp.corr(eur)
        if leader == 2 and lagger == 3:
            xcov = gbp.corr(jpy)
        if leader == 3 and lagger == 0:
            xcov = jpy.corr(usd)
        if leader == 3 and lagger == 1:
            xcov = jpy.corr(eur)
        if leader == 3 and lagger == 2:
            xcov = jpy.corr(gbp)

        return xcov

    """
    This method calculates the lagged cross correlation between two BTC-currency pairs. Following int values allow 
    access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY

    lag:    amount of lags (up to 24 makes sense with hourly data to get daily effects in crosscorr)
    lagger: lagged variable
    """

    def getCrossCorrelation(self, lagger, btcusd, btceur, btcgbp, btcjpy, lag):
        # pd.set_option("display.max_rows", None, "display.max_columns", None)
        date, df, df2UpsideDown, usd = self.normaliseDfForCc(btceur, btcgbp, btcjpy, btcusd)
        df2UpsideDown = self.transformDfForLag(date, df, df2UpsideDown, lag, usd)
        df = self.concatDf(date, df2UpsideDown, usd)

        usd = df['BTCUSD']
        eur = df['BTCEUR']
        gbp = df['BTCGBP']
        jpy = df['BTCJPY']

        xcov = self.defineLeaderLagger(usd, eur, gbp, jpy, 0, lagger)
        print(xcov)
        return (xcov)

    """
    This is a helper method that concatenates the dates and CS values of BTCUSD with the other currencies + their dates.
    """
    def concatDf(self, date, df2UpsideDown, usd):
        df = pd.concat([date, usd], axis=1, join='outer')
        df = pd.concat([df, df2UpsideDown], axis=1, join='outer')
        return df

    """
    This is a helper method that do transformations to the dataframe for the lag that should be used.
    """
    def transformDfForLag(self, date, df, df2UpsideDown, lag, usd):
        df2UpsideDown = df2UpsideDown.drop(df.index[0: lag])
        df2UpsideDown.reset_index(drop=True, inplace=True)
        usd.drop(usd.tail(lag).index, inplace=True)
        date.drop(date.tail(lag).index, inplace=True)
        return df2UpsideDown

    """
    This is a helper method that do transformations to the dataframe before it can be used for calculating the 
    crosscorr.
    """
    def normaliseDfForCc(self, btceur, btcgbp, btcjpy, btcusd):
        df = self.getStandardisedAr(btcusd, btceur, btcgbp, btcjpy).reset_index()
        df2 = self.getStandardisedAr(btcusd, btceur, btcgbp, btcjpy).reset_index()
        dfUpsideDown = df.loc[::-1]
        df2UpsideDown = df2.loc[::-1]
        dfUpsideDown.reset_index(drop=True, inplace=True)
        df2UpsideDown.reset_index(drop=True, inplace=True)
        date = dfUpsideDown['Date']
        usd = dfUpsideDown['BTCUSD']
        df2UpsideDown.drop('BTCUSD', inplace=True, axis=1)
        return date, df, df2UpsideDown, usd

    """
    This method shows a graph with the pearson correlaton coefficient on the y-axis and the lags up tp 120 on the 
    x-Axis. It shows the cross-correlation between all BTC-currency pairs with BTC/USD as leading variable.     
    """
    def crossCorrGraph(self, btcusd, btceur, btcgbp, btcjpy):

        print('The graph will be shown when the number 168 is reached')
        crosscorreur = []
        crosscorrgbp = []
        crosscorrjpy = []
        lag = []
        for i in range(168):
            correur = self.getCrossCorrelation(1, btcusd, btceur, btcgbp, btcjpy, i)
            corrgbp = self.getCrossCorrelation(2, btcusd, btceur, btcgbp, btcjpy, i)
            corrjpy = self.getCrossCorrelation(3, btcusd, btceur, btcgbp, btcjpy, i)
            crosscorreur.append(correur)
            crosscorrgbp.append(corrgbp)
            crosscorrjpy.append(corrjpy)
            lag.append(i)
            print(i)

        self.plotCrossCorr(crosscorreur, crosscorrgbp, crosscorrjpy, lag)

    """
    This is a helper method that defines all attributes for plotting the corosscorr in a graph
    """
    def plotCrossCorr(self, crosscorreur, crosscorrgbp, crosscorrjpy, lag):
        plt.xlabel('Verzögerung')
        plt.ylabel('Pearson Korrelationskoeffizient')
        plt.title('Corwin und Schultz Kreuzkorrelation')
        plt.plot(lag, crosscorreur)
        plt.plot(lag, crosscorrgbp)
        plt.plot(lag, crosscorrjpy)
        plt.legend(['BTC/USD - BTC/EUR', 'BTC/USD - BTC/GBP', 'BTC/USD - BTC/JPY'])
        plt.show()








