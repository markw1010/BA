import itertools
import sys

import np as np
import numpy
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import autocorrelation_plot
from collections import OrderedDict
import statsmodels.formula.api as smf

from patsy.highlevel import dmatrices
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

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
    
    Returns    pandas dataframe containing AH values for each currency pair and date as int
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
        dataframe['Date'] = dataframe['Date'].astype('datetime64')  # to set date as integer values
        dataframe = dataframe.set_index('Date')

        print(dataframe)
        return dataframe

    """
    This method plots all the Amihud values in one graph with the date on the x-axis and the value on the y-axis
    """
    def amihudGraph(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        dataframe = self.getNormalizedDataframe(fileEUR, fileGBP, fileJPY, fileUSD, int)
        dataframe = self.setDateIndex(dataframe)
        self.pltShow(dataframe, int)

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
        date, usd, eur, gbp, jpy = self.cutAhArray(fileUSD, fileEUR, fileGBP, fileJPY)
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
        plt.xlabel('Date')
        plt.ylabel('Values')
        self.chooseTitle(int)
        plt.plot(dataframe)
        plt.show()

    """
    This method plots the autocorrelation of the amihud values in a graph. Following int values allow access to 
    following currency pairs:
    
    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
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
    This method gets the autocorrelation of the amihud values in a graph Following int values allow access to following 
    currency pairs:

    int = 0: BTC/USD
    int = 1: BTC/EUR
    int = 2: BTC/GBP
    int = 3: BTC/JPY
    """
    def getAutocorrGraph(self, fileEUR, fileGBP, fileJPY, fileUSD, int):
        data = self.calcAutocorrGraph(fileEUR, fileGBP, fileJPY, fileUSD, int)
        return data

    """
    This is a helper method to set a title for autocorrelation graph of the autocorrGraph method, depending on what 
    currency should be shown. 0 refers to USD, 1 refers to EUR, 2 refers GBP and 3 refers to JPY
    """
    def chooseTitle(self, int):
        if int == 0:
            plt.title('Amihud liquidity measure USD')
        if int == 1:
            plt.title('Amihud liquidity measure EUR')
        if int == 2:
            plt.title('Amihud liquidity measure GBP')
        if int == 3:
            plt.title('Amihud liquidity measure JPY')

    """
    This is a helper method to for the autocorrGraph method to choose a currency pair. 0 refers to USD, 1 refers to EUR, 
    2 refers GBP and 3 refers to JPY
    """
    def chooseCurrencyPair(self, date, eur, gbp, int, jpy, usd):
        if int == 0:
            ahValues = {
                'Date': date,
                'BTCUSD': usd,
            }
        if int == 1:
            ahValues = {
                'Date': date,
                'BTCEUR': eur,
            }
        if int == 2:
            ahValues = {
                'Date': date,
                'BTCGBP': gbp,
            }
        if int == 3:
            ahValues = {
                'Date': date,
                'BTCJPY': jpy,
            }

        print(int)
        return ahValues

    """
    This method prints the pandas table where the values are aggregated by the month
    """
    def getMonthlyAggregated(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        dataset = self.getNormalizedDataframe(fileEUR, fileGBP, fileJPY, fileUSD, int)

        dataset = self.setDateIndex(dataset)

        dataset = dataset.resample('M').mean()

        #print(dataset[dataset.columns[0]].count())
        #print(dataset)
        #print(int)

        return dataset

    def addLaggedVariableColumns(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        df_lagged = self.getMonthlyAggregated(fileUSD, fileEUR, fileGBP, fileJPY, int)

        if int == 0:
            for i in range(1, 13, 1):
                df_lagged['BTCUSD_LAG_' + str(i)] = df_lagged['BTCUSD'].shift(i)
        if int == 1:
            for i in range(1, 13, 1):
                df_lagged['BTCEUR_LAG_' + str(i)] = df_lagged['BTCEUR'].shift(i)
        if int == 2:
            for i in range(1, 13, 1):
                df_lagged['BTCGBP_LAG_' + str(i)] = df_lagged['BTCGBP'].shift(i)
        if int == 3:
            for i in range(1, 13, 1):
                df_lagged['BTCJPY_LAG_' + str(i)] = df_lagged['BTCJPY'].shift(i)

        #print(df_lagged.head(15))

        for i in range(0, 12, 1):                               # The first 12 rows contain NaNs introduced by the
            df_lagged = df_lagged.drop(df_lagged.index[0])      # shift function. Let’s remove these 12 rows.

        print(df_lagged.head())
        return df_lagged


    def filterDataset(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        df_lagged = self.addLaggedVariableColumns(fileUSD, fileEUR, fileGBP, fileJPY, int)
        split_index = round(len(df_lagged) * 0.8)
        split_date = df_lagged.index[split_index]
        df_train = df_lagged.loc[df_lagged.index <= split_date].copy()
        df_test = df_lagged.loc[df_lagged.index > split_date].copy()

        return df_test, df_train

    def lagCombinations(self):

        lag_combinations = OrderedDict()
        l = list(range(1, 13, 1))

        for i in range(1, 13, 1):
            for combination in itertools.combinations(l, i):
                lag_combinations[combination] = 0.0

        print('Number of combinations to be tested: ' + str(len(lag_combinations)))

        return lag_combinations

    def linearRegressionModel(self, fileUSD, fileEUR, fileGBP, fileJPY, int):

        lag_combinations = self.lagCombinations()
        df_test , df_train = self.filterDataset(fileUSD, fileEUR, fileGBP, fileJPY, int)
        expr_prefix = 'BTCUSD ~ '

        min_aic = sys.float_info.max
        best_expr = ''
        best_olsr_model_results = None

        # Iterate over each combination
        for combination in lag_combinations:
            expr = expr_prefix
            i = 1
            # Setup the model expression using patsy syntax
            for lag_num in combination:
                if i < len(combination):
                    expr = expr + 'BTCUSD_LAG_' + str(lag_num) + ' + '
                else:
                    expr = expr + 'BTCUSD_LAG_' + str(lag_num)

                i += 1

            print('Building model for expr: ' + expr)

            # Carve out the X,y vectors using patsy. We will use X_test, y_test later for testing the model.
            y_test, X_test = dmatrices(expr, df_test, return_type='dataframe')

            # Build and train the OLSR model on the training data set
            olsr_results = smf.ols(expr, df_train).fit()

            # Store it's AIC value
            lag_combinations[combination] = olsr_results.aic

            # Keep track of the best model (the one with the lowest AIC score) seen so far
            if olsr_results.aic < min_aic:
                min_aic = olsr_results.aic
                best_expr = expr
                best_olsr_model_results = olsr_results

            #print('AIC=' + str(lag_combinations[combination]))

        print(best_olsr_model_results.summary())