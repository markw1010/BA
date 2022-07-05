import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
import matplotlib.dates as mdates

"""
This class provides all necessary methods and variables to calculate the Corwin and Schultz (CS) liquidity estimator for 
a daily, hourly or minutely cvs datasets respectively. Moreover it provides methods to calculate the autocorreltion and
crosscorrelation of different BTC-currency pairs.

Corwin, S., Schultz, P., 2012. A simple way to estimate bid-ask spreads from daily 	high and low prices. The Journal of 
Finance, Volume 67, Issue 2. 719-760
"""


class CorwinSchultz:

    denominatorAlpha = 3 - 2 * 2 ** 0.5

    np.arr = []

    """
    This method prints only the value for the CS estimator on the console.
    
    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the CS estimator will be printed on the console 
    """
    def corwinSchultzValueOnly(self, file, currency):

        CS = self.calculateCSValue(file)

        print(currency + ' CS:')
        print(CS)

    """
    This method is only implemented for the use of comparison to the CS estimator in the comparison class.
    """
    def corwinSchultzComparison(self, file, currency):

        CS = self.calculateCSValue(file)

        print(currency + ' CS:')
        print(CS)

    """
        this method prints the values for the CS alpha, CS beta, CS gamma, CS_i,i+1, CS and other. 

        Ensures:    the values for the CS alpha, CS beta, CS gamma, CS_i,i+1, sum(CS_i,i+1), len(CS_i,i+1) and CS will 
                    be printed on the console
        """
    def printCS(self, file, currency):

        CS = self.calculateCSValue(file)

        print('Alpha:')
        print(self.getAlpha(file))
        print('-----------')
        print('Beta:')
        print(self.getBeta(file))
        print('-----------')
        print('Gamma:')
        print(self.getGamma(file))
        print('-----------')
        print('CS_i,i+1:')
        print(self.calculateCSArray(file))
        print('-----------')
        print('sum(CS_i,i+1):')
        print(np.sum(self.calculateCSArray(file)))
        print('-----------')
        print('len(CS_i,i+1):')
        print(len(self.calculateCSArray(file)))
        print('-----------')
        print(currency + ' CS:')
        print(CS)

    """
    This method returns the value for the CS estimator in period t calculating the unweighted average of all CS 
    estimators for adjacent subintervals in t.
    
    Requires:   len(CSii1) > 0
    
    Ensures:    CS is a numerical value 
    """
    def calculateCSValue(self, file):
        CSii1 = self.calculateCSArray(file)
        sum = np.sum(CSii1)
        amount = len(CSii1)
        CS = sum / amount
        return CS

    """
    this method calculates the CS_i,i+1 Array which contains the CS estimator for two adjacent intervals i and 
    i+1.

    Requires:   len(alpha) > 0
                denominator should not contain a zero value item
                alpha should only contain numbers

    Ensures:    CSii1 only contains numerical items
    
    Returns:    CSii1 - Array which contains the CS estimator for two adjacent intervals i and i+1       
    """
    # TODO def programming: can e to the power of x can equal -1?
    def calculateCSArray(self, file):

        alpha = self.getAlpha(file)
        expAlpha = np.exp(alpha)
        counterA = np.subtract(expAlpha, 1)
        counter = np.multiply(counterA, 2)
        denominator = np.add(expAlpha, 1)

        CSii1 = [counter / denominator for counter, denominator in zip(counter, denominator)]

        return CSii1

    """
    This method calculates the alpha of the CS estimator. Alpha is divided into two parts and it is calculated by 
    subtracting the first from the second part element wise.
    
    Requires:   len(firstTerm) == len(secondTerm)
    
    Ensures:    alpha only contains numerical elements
    
    Returns:    alpha - Array
    """
    def getAlpha(self, file):

        firstTerm = self.alphaFirstTerm(file)
        secondTerm = self.alphaSecondTerm(file)

        alpha = [frstTerm - secTerm for frstTerm, secTerm in zip(firstTerm, secondTerm)]

        return alpha

    """
    This method calculates the first term of the CS alpha. It divides the gamma value from a static constant which is 
    declared as public variable called denominatorAlpha an then rooted. 
    
    Requires:   all items in gamma != 0
                denominatorAlpha != 0
                all items in gamma should be either all positive or all negative, depending if the denominatorAlpha is 
                positive or negative
                
    Ensures:    secondTerm contains online positive numerical items 
    
    Returns:    secondTerm - Array with all values for the second term of the CS alpha 
    """
    def alphaSecondTerm(self, file):

        gamma = self.getGamma(file)

        secondTermNoRoot = np.divide(gamma, self.denominatorAlpha)
        secondTerm = np.power(secondTermNoRoot, 0.5)

        return secondTerm

    """
    This method calculates the second term of the CS alpha. It calculates the rooted beta multiplied by 2 and just the 
    rooted beta and divides them each.
    
    Requires:   all items in rootTtBeta and rootBeta are bigger or equal to 0
                len(rootTtBeta) == len(rootBeta)
                
    Ensures:    firstTerm contains online positive numerical items    
    
    Returns:    firstTerm - Array with all values for the first term of the CS alpha 
    """
    def alphaFirstTerm(self, file):

        twoTimesBeta = np.multiply(self.getBeta(file), 2)
        beta = self.getBeta(file)

        rootTtBeta = np.power(twoTimesBeta, 0.5)
        rootBeta = np.power(beta, 0.5)

        counterFirstTerm = [rootTtBeta - rootBeta for rootTtBeta, rootBeta in zip(rootTtBeta, rootBeta)]
        firstTerm = np.divide(counterFirstTerm, self.denominatorAlpha)

        return firstTerm

    """
    This method calculates the CS beta and returns it. Therefore it adds the two terms where the second term equals the
    first term but the values are shifted by +1. Therefore the first element of the secondTerm array is removed. To 
    calculate the beta, the first term is added to the second term.

    Requires:   all items in highDivLow should be greater than 0

    Ensures:    beta only contains numerical items
    
    Returns:    beta - Array which contains all beta items
    """
    # TODO Exception handling if item in open is 0!
    def getBeta(self, file):

        highDivLow = self.highDivLow(file)
        ln = numpy.log(highDivLow)
        firstTerm = numpy.power(ln, 2)
        secondTerm = np.delete(np.copy(firstTerm), 0)

        beta = [x + y for x, y in zip(firstTerm, secondTerm)]

        return beta

    """
    This method takes an array and makes two arrays of it while in the array called arri1 the first element is removed 
    and on the arrModified array the last element is removed. Then both arrays are compared element wise and the the 
    bigger item will be put into the max array
    
    Requires:   The input Array has to contain numbers only  
                The input Array has to have at least 2 Items 
                
    Ensures:    max contains at least two elements 
    
    Returns:    max - Array which contains the maximum of the shifted compared input array
    """
    def getMaxPrice(self, arr):

        arrModified = np.delete(arr, -1)
        arri1 = np.delete(arr, 0)

        max = np.maximum(arrModified, arri1)

        return max

    # TODO Error handling if div by 0!
    def getGamma(self, file):
        high = self.getHighCS(file)
        low = self.getLowCS(file)

        hii1 = self.getMaxPrice(high)

        lii1 = self.getMaxPrice(low)

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

    """
    This method divides all items in np.highFlt from the items in np.lowFlt. np.highFlt and np.lowFlt contain all the 
    high and low prices in the provided cvs respectively. 
    
    Requires:   len(np.highFlt) == len(np.lowFlt)
                no item in np.lowFlt should be 0

    Ensures:    highDivLow only contains numerical values 
    
    Returns:    highDivLow - Array which contains all items of np.highFlt divided by np.lowFlt
    """
    def highDivLow(self, file):
        high = self.getHighCS(file)
        low = self.getLowCS(file)

        np.seterr(invalid='ignore')  # This tells NumPy to hide any warning with some “invalid” message in it
        highDivLow = np.divide(high, low, out=np.zeros_like(high), where=low != 0)
        highDivLow = highDivLow[
            ~numpy.isnan(highDivLow)]  # to remove all nan values (caused by missing low prices)
        return highDivLow

    """
    This method returns an array with the high prices of BTC in a specific time period and currency filtered out of a 
    cvs file

    Requires:   the column with the data for the high prices has to be called 'high' in the cvs file
                The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    high only contains string elements
    
    Returns:    high - Array will be returned with all the high data represented as strings
    """

    def getHighCS(self, file):
        high = file['high'].to_numpy()

        return high

    """
    This method returns an array with the low prices of BTC in a specific time period and currency  filtered out of a 
    cvs file

    Requires:   The cvs file has to be formatted so that it can be read
                the column with the data for the close prices has to be called 'low' in the cvs file                    
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    low only contains string elements
    
    Returns:    low - Array will be returned with all the low data represented as strings
    """

    def getLowCS(self, file):

        low = file['low'].to_numpy()

        return low

    """
    this method takes four arrays which are containing the cs values in all representative currency pairs and 
    figures out which array contains the fewest data.

    Requires:   

    Ensures:    An integer value above -1 will be return

    Returns:    the amount of data that the smallest array contains
    """
    def getSmallest(self, btcusd, btceur, btcgbp, btcjpy):

        usd = len(self.calculateCSArray(btcusd))
        eur = len(self.calculateCSArray(btceur))
        gbp = len(self.calculateCSArray(btcgbp))
        jpy = len(self.calculateCSArray(btcjpy))

        csValues = (usd, eur, gbp, jpy)
        smallest = csValues.index(min(csValues))

        return csValues[smallest]

    """
    This method cuts all four arrays to the amount of data that contains the smallest of the four arrays. The arrays 
    are containing the AR values and each array represent one currency pair

    Requires:

    Ensures:    four arrays with the exact same amount of data will be returned

    Returns:    cuttet arrays on the smallest amount of data of each currency pair 
    """
    def cutCsArray(self, usd, eur, gbp, jpy):

        #smallestArray = self.getSmallest(usd, eur, gbp, jpy)

        dateUSD = usd['date'].to_numpy()
        dateEUR = eur['date'].to_numpy()
        dateGBP = gbp['date'].to_numpy()
        dateJPY = jpy['date'].to_numpy()

        dateUSD = np.delete(dateUSD, 0)
        dateEUR = np.delete(dateEUR, 0)
        dateGBP = np.delete(dateGBP, 0)
        dateJPY = np.delete(dateJPY, 0)

        # print('usd')
        #print(len(dateUSD))
        usd = self.calculateCSArray(usd)
        #print(len(usd))
        # print('eur')
        # print(len(dateEUR))
        eur = self.calculateCSArray(eur)
        # print(len(eur))
        # print('gbp')
        # print(len(dateGBP))
        gbp = self.calculateCSArray(gbp)
        # print(len(gbp))
        # print('jpy')
        # print(len(dateJPY))
        jpy = self.calculateCSArray(jpy)
        # print(len(jpy))

        usd = pd.DataFrame({'date': dateUSD,
                            'BTCUSD': usd})
        eur = pd.DataFrame({'date': dateEUR,
                            'BTCEUR': eur})
        gbp = pd.DataFrame({'date': dateGBP,
                            'BTCGBP': gbp})
        jpy = pd.DataFrame({'date': dateJPY,
                            'BTCJPY': jpy})

        usd = usd.set_index('date')
        eur = eur.set_index('date')
        gbp = gbp.set_index('date')
        jpy = jpy.set_index('date')

        df = usd.join(eur)
        df = df.join(gbp)
        df = df.join(jpy)

        df.dropna(subset=["BTCUSD"], inplace=True)
        df.dropna(subset=["BTCEUR"], inplace=True)
        df.dropna(subset=["BTCGBP"], inplace=True)
        df.dropna(subset=["BTCJPY"], inplace=True)

        return df

    def printCsValues(self, usd, eur, gbp, jpy):
        df = self.cutCsArray(usd, eur, gbp, jpy)
        print(df)

    """
    This method gets the standardised arrays containing the cs values for each currency pair
    
    Returns    pandas dataframe containing CS values for each currency pair and date as int
    """
    def getStandardisedCS(self, fileUSD, fileEUR, fileGBP, fileJPY):

        df = self.cutCsArray(fileUSD, fileEUR, fileGBP, fileJPY)

        csValues = {
            'Date': df.index,
            'BTCUSD': df['BTCUSD'],
            'BTCEUR': df['BTCEUR'],
            'BTCGBP': df['BTCGBP'],
            'BTCJPY': df['BTCJPY']
        }

        dataframe = pd.DataFrame(csValues)
        dataframe['Date'] = dataframe['Date'].astype('datetime64')  # to set date as integer values
        dataframe = dataframe.set_index('Date')

        return dataframe

    """
    This method prints some of the CS values
    """
    def printCsValues(self, fileUSD, fileEUR, fileGBP, fileJPY):
        values = self.getStandardisedCS(fileUSD, fileEUR, fileGBP, fileJPY)
        print(values)

    """
    This method prints all of the CS values
    """
    def printAllCsValues(self, fileUSD, fileEUR, fileGBP, fileJPY):
        values = self.getStandardisedCS(fileUSD, fileEUR, fileGBP, fileJPY)
        #pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(values.to_string())

    """
    This method plots all the CS values in one graph with the date oin the x-axis and the value on the y-axis
    """
    def csGraph(self, fileUSD, fileEUR, fileGBP, fileJPY):

        #dataframe = self.getNormalizedDataframe(fileEUR, fileGBP, fileJPY, fileUSD, int)
        #dataframe = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        dataframe = self.cutCsArray(fileUSD, fileEUR, fileGBP, fileJPY)

        dataframe.index = pd.to_datetime(dataframe.index)
        usd = dataframe['BTCUSD']
        eur = dataframe['BTCEUR']
        gbp = dataframe['BTCGBP']
        jpy = dataframe['BTCJPY']

        plt.figure()
        plt.plot(usd)
        plt.plot(eur)
        plt.plot(gbp)
        plt.plot(jpy)
        ax = plt.gca()

        ax.xaxis.set_major_locator(mdates.HourLocator(interval=6))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
        plt.gcf().autofmt_xdate()

        plt.xlabel('Datum')
        plt.ylabel('Wert')
        plt.legend(['BTC/USD', 'BTC/EUR', 'BTC/GBP', ' BTC/JPY'])
        plt.title('Corwin und Schultz Liquiditätsmaß - absolute Werte [minütlich]')
        #plt.plot(dataframe)
        plt.show()


        #dataframe = self.setDateIndex(dataframe)
        #print(dataframe)
        #self.pltShow(dataframe, int)

    """
    This method exports all CS values to an Excel file
    """
    def csToExcel(self, fileUSD, fileEUR, fileGBP, fileJPY):
        values = self.getStandardisedCS(fileUSD, fileEUR, fileGBP, fileJPY)
        values.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/CS.xlsx', index=True)

    """
    This method helps to get a dataframe of cs values of one currency pair, depending on the int value that is 
    given. Therefore the cs values of each currency pair has to be standardised on the same length. Following int 
    values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def getNormalizedDataframe(self, fileEUR, fileGBP, fileJPY, fileUSD, int):
        date, usd, eur, gbp, jpy = self.cutCsArray(fileUSD, fileEUR, fileGBP, fileJPY)
        dataframe = self.chooseCurrencyPair(date, eur, gbp, int, jpy, usd)
        return dataframe

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
    In this method are all the settings defined to plot a dataframe with some kind of numerical values on y-axis and 
    date values on the x-axis. Following int values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def pltShow(self, dataframe, int):
        plt.xlabel('Datum')
        plt.ylabel('Wert')
        self.chooseTitle(int)
        plt.plot(dataframe)
        plt.show()

    """
    This method plots the autocorrelation of the cs values in a graph
    """
    def showAutocorrGraph(self, fileUSD, fileEUR, fileGBP, fileJPY):

        self.calcAutocorrGraph(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.show()

    """
    This method calculates the autocorrelation of of past BTC liquidity data for each BTC currency pair. Date values are 
    the index. Following int values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def calcAutocorrGraph(self, fileEUR, fileGBP, fileJPY, fileUSD):
        #dataframe = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        dataframe = self.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)

        for variable in dataframe.columns:
            autocorr = autocorrelation_plot(dataframe[variable], label= variable)

        autocorr.set_xlim([0, 30])
        autocorr.set(xlabel="Verzögerung", ylabel="Autokorrelation", title='Corwin und Schultz Autokorrelation [täglich]')

        #self.chooseTitle(int)

    """
    This method returns a dataframe with two columns. one column contains all date values and the other column contains 
    all cs values. the Dataframe is standardised on the length of the smallest amount of data of all of the BTC-
    currency pairs. The date values are the index. Following int values allow access to following currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def getCsValues(self, fileEUR, fileGBP, fileJPY, fileUSD, int):
        csValues = self.getNormalizedDataframe(fileEUR, fileGBP, fileJPY, fileUSD, int)
        dataframe = pd.DataFrame(csValues)
        dataframe['Date'] = dataframe['Date'].astype('datetime64')  # to set date as integer values
        dataframe = dataframe.set_index('Date')
        return dataframe

    """
    This is a helper method to set a title for autocorrelation graph of the autocorrGraph method, depending on what 
    currency should be shown. 0 refers to USD, 1 refers to EUR, 2 refers GBP and 3 refers to JPY
    """
    def chooseTitle(self, int):
        if int == 0:
            plt.title('Corwin und Schultz Liquiditätsmaß BTC/USD')
        if int == 1:
            plt.title('Corwin und Schultz Liquiditätsmaß BTC/EUR')
        if int == 2:
            plt.title('Corwin und Schultz Liquiditätsmaß BTC/GBP')
        if int == 3:
            plt.title('Corwin und Schultz Liquiditätsmaß BTC/JPY')

    """
    This is a helper method to for the autocorrGraph method to choose a currency pair. 0 refers to USD, 1 refers to EUR, 
    2 refers GBP and 3 refers to JPY
    """
    def chooseCurrencyPair(self, date, eur, gbp, int, jpy, usd):
        if int == 0:
            csValues = {
                'Date': date,
                'BTCUSD': usd,
            }
        if int == 1:
            csValues = {
                'Date': date,
                'BTCEUR': eur,
            }
        if int == 2:
            csValues = {
                'Date': date,
                'BTCGBP': gbp,
            }
        if int == 3:
            csValues = {
                'Date': date,
                'BTCJPY': jpy,
            }
        return csValues

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
    This method prints the CS values of one BTC-currency pair. Following int values allow access to following 
    currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def getCurrencyValues(self, int, fileUSD, fileEUR, fileGBP, fileJPY):
        df = self.getStandardisedCS(fileUSD, fileEUR, fileGBP, fileJPY)

        if int == 0:
            largest = df['BTCUSD']
        if int == 1:
            largest = df['BTCEUR']
        if int == 2:
            largest = df['BTCGBP']
        if int == 3:
            largest = df['BTCJPY']

        return largest

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
        #pd.set_option("display.max_rows", None, "display.max_columns", None)
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
        df = self.getStandardisedCS(btcusd, btceur, btcgbp, btcjpy).reset_index()
        df2 = self.getStandardisedCS(btcusd, btceur, btcgbp, btcjpy).reset_index()
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

        #crosscorreur, crosscorrgbp, crosscorrjpy, lag = self.crossCorrData(btceur, btcgbp, btcjpy, btcusd)

        crosscorreur = []
        crosscorrgbp = []
        crosscorrjpy = []
        lag = []
        for i in range(31):
            print(i)
            correur = self.getCrossCorrelation(1, btcusd, btceur, btcgbp, btcjpy, i)
            corrgbp = self.getCrossCorrelation(2, btcusd, btceur, btcgbp, btcjpy, i)
            corrjpy = self.getCrossCorrelation(3, btcusd, btceur, btcgbp, btcjpy, i)
            crosscorreur.append(correur)
            crosscorrgbp.append(corrgbp)
            crosscorrjpy.append(corrjpy)
            lag.append(i)


        self.plotCrossCorr(crosscorreur, crosscorrgbp, crosscorrjpy, lag)

        df = pd.DataFrame({'lag': lag,
                            'BTC/USD-BTC/EUR': crosscorreur,
                            'BTC/USD-BTC/GBP': crosscorrgbp,
                            'BTC/USD-BTC/JPY': crosscorrjpy})

        df.set_index('lag')
        df.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/CrossCorr/CrossCorrCS.xlsx', index=True)

        print(df)

    """
    This is a helper method that defines all attributes for plotting the corosscorr in a graph
    """
    def plotCrossCorr(self, crosscorreur, crosscorrgbp, crosscorrjpy, lag):
        plt.xlabel('Verzögerung')
        plt.ylabel('Pearson Korrelationskoeffizient')
        plt.title('Corwin und Schultz Kreuzkorrelation [täglich]')
        plt.plot(lag, crosscorreur)
        plt.plot(lag, crosscorrgbp)
        plt.plot(lag, crosscorrjpy)
        plt.legend(['BTC/USD - BTC/EUR', 'BTC/USD - BTC/GBP', 'BTC/USD - BTC/JPY'])
        plt.show()

    """
    This is a helper method which saves the cross correlations with all BTC-currency pairs with the currency pair BTCUSD 
    as leading variable in arrays up to lag 168.
    """
    # def crossCorrData(self, btceur, btcgbp, btcjpy, btcusd):
    #     crosscorreur = []
    #     crosscorrgbp = []
    #     crosscorrjpy = []
    #     lag = []
    #     for i in range(61):
    #         correur = self.getCrossCorrelation(1, btcusd, btceur, btcgbp, btcjpy, i)
    #         corrgbp = self.getCrossCorrelation(2, btcusd, btceur, btcgbp, btcjpy, i)
    #         corrjpy = self.getCrossCorrelation(3, btcusd, btceur, btcgbp, btcjpy, i)
    #         crosscorreur.append(correur)
    #         crosscorrgbp.append(corrgbp)
    #         crosscorrjpy.append(corrjpy)
    #         lag.append(i)
    #         print(i)
    #
    #     print(crosscorreur)
    #     return crosscorreur, crosscorrgbp, crosscorrjpy, lag

    def getBiggestUSD(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        df.drop('BTCEUR', inplace=True, axis=1)
        df.drop('BTCGBP', inplace=True, axis=1)
        df.drop('BTCJPY', inplace=True, axis=1)

        largest = df.nlargest(10, 'BTCUSD')
        largest.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/Biggest/CSLargestUSD.xlsx', index=True)

        print(largest)

    def getBiggestEUR(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        df.drop('BTCUSD', inplace=True, axis=1)
        df.drop('BTCGBP', inplace=True, axis=1)
        df.drop('BTCJPY', inplace=True, axis=1)

        largest = df.nlargest(10, 'BTCEUR')
        largest.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/Biggest/CSLargestEUR.xlsx', index=True)

        print(largest)

    def getBiggestGBP(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        df.drop('BTCUSD', inplace=True, axis=1)
        df.drop('BTCEUR', inplace=True, axis=1)
        df.drop('BTCJPY', inplace=True, axis=1)

        largest = df.nlargest(10, 'BTCGBP')
        largest.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/Biggest/CSLargestGBP.xlsx', index=True)

        print(largest)

    def getBiggestJPY(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        df.drop('BTCUSD', inplace=True, axis=1)
        df.drop('BTCGBP', inplace=True, axis=1)
        df.drop('BTCEUR', inplace=True, axis=1)

        largest = df.nlargest(10, 'BTCJPY')
        largest.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/Biggest/CSLargestJPY.xlsx', index=True)

        print(largest)

    def getBiggest(self, fileEUR, fileGBP, fileJPY, fileUSD):
        self.getBiggestUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        self.getBiggestEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        self.getBiggestGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        self.getBiggestJPY(fileEUR, fileGBP, fileJPY, fileUSD)

    def autocorrData(self, fileEUR, fileGBP, fileJPY, fileUSD):
        #df = self.getStandardisedCS(fileEUR, fileGBP, fileJPY, fileUSD)
        df = self.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)

        usd = df['BTCUSD']
        eur = df['BTCEUR']
        gbp = df['BTCGBP']
        jpy = df['BTCJPY']

        index = []
        autocorrUSD = []
        autocorrEUR = []
        autocorrGBP = []
        autocorrJPY = []

        for i in range(31):
            usdAutocorr = usd.autocorr(lag=i)
            eurAutocorr = eur.autocorr(lag=i)
            gbpAutocorr = gbp.autocorr(lag=i)
            jpyAutocorr = jpy.autocorr(lag=i)

            autocorrUSD.append(usdAutocorr)
            autocorrEUR.append(eurAutocorr)
            autocorrGBP.append(gbpAutocorr)
            autocorrJPY.append(jpyAutocorr)
            index.append(i)

        df = pd.DataFrame({'Verschiebung': index,
                           'BTCUSD': autocorrUSD,
                           'BTCEUR': autocorrEUR,
                           'BTCGBP': autocorrGBP,
                           'BTCJPY': autocorrJPY})
        print(df)

        df.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/Autocorr/CSAutocorr.xlsx', index=True)





















