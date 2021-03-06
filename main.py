import pandas as pd

from AbdiRanaldo import AbdiRanaldo
from Amihud import Amihud
from Comparison import Comparison
from CorwinSchultz import CorwinSchultz
from Filter import Filter
from LeadLag import LeadLag

"""
This program will take a cvs file which contains daily, hourly or minutely high and low, open and close as well as other 
data respectively provided by Bitfinex. It will filter and show all the relevant information needed, to calculate the 
liquidity measures of Amihud (2002), Corwin and Schultz (2012) and Abdi and Ranaldo (2017). The Liquidity estimators are 
inspired by the measures which are presented in the following paper:

Amihud, Y., 2002. Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets 5. 
31-56

Corwin, S., Schultz, P., 2012. A simple way to estimate bid-ask spreads from daily 	high and low prices. The Journal of 
Finance, Volume 67, Issue 2. 719-760

Abdi, F., Ranaldo, A., 2017. A simple estimation of bid-ask spreads from daily close, high, and low prices. The Review 
of Financial Studies, Volume 30, Issue 12, December 2017. 4437-4480

Please note that you should only uncomment one line of code at the the same time, otherwise the program will not work!
Please make sure, that you choose the right csv file to analyse in line 28 and 29 of this file
Please note that all the notations for the estimators are from the following paper:

Brauneis, A., Mestel, R., Riordan, R., Theissen, E., 2021. How to measure the liquidity of cryptocurrency markets? 
Journal of Banking and Finance 124 (2021) 106041. 1-26

Author: Mark Wagner

University of Stuttgart
"""

# Prototype dataset
btcusd = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCUSD_d.csv')
btceur = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCEUR_d.csv')
btcjpy = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCJPY_d.csv')
btcgbp = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCGBP_d.csv')

amihud = Amihud()
cs = CorwinSchultz()
comp = Comparison()
ar = AbdiRanaldo()
filter = Filter()
ll = LeadLag()

# Uncomment this line of code to show the whole dataset on the console
#filter.print_full(btcusd)
# filter.print_full(btceur)
# filter.print_full(btcjpy)
# filter.print_full(btcgbp)

# Uncomment this lines of code to show the dataset on the console
# print(btcusd)
# print(btceur)
# print(btcjpy)
# print(btcgbp)

# TODO nice printing
# Uncomment this line of code to show the detailed Amihud calculation on the console
# amihud.amihudDetailed(btcusd, 'USD') # TODO fail
# amihud.amihudDetailed(btceur, 'EUR')
# amihud.amihudDetailed(btcjpy, 'JPY')
# amihud.amihudDetailed(btcgbp, 'GBP')
# amihud.getAmihudExpression(btcusd, 'USD')

# Uncomment this line of code to show the detailed CS calculation on the console
# cs.printCS(btcusd, 'USD')
# cs.printCS(btceur, 'EUR')
# cs.printCS(btcjpy, 'JPY')
# cs.printCS(btcgbp, 'GBP')
# cs.cutCsArray(btcusd, btceur, btcgbp, btcjpy)
# cs.printstandardisedCS(btcusd, btceur, btcgbp, btcjpy)

# TODO JPY values checking
# Uncomment this line of code to show the single Amihud value on the console
# amihud.amihudValueOnly(btcusd, 'USD')
# amihud.amihudValueOnly(btceur, 'EUR')
# amihud.amihudValueOnly(btcjpy, 'JPY')
# amihud.amihudValueOnly(btcgbp, 'GBP')
# amihud.printStandardisedAh(btcusd, btceur, btcgbp, btcjpy)

# TODO Werte pr??fen
# Uncomment this line of code to show the single CS value on the console
# cs.corwinSchultzValueOnly(btcusd, 'USD')
# cs.corwinSchultzValueOnly(btceur, 'EUR')
# cs.corwinSchultzValueOnly(btcjpy, 'JPY')
# cs.corwinSchultzValueOnly(btcgbp, 'GBP')

# Uncomment this line of code to show the single AR value on the console
# ar.abdiRanaldoValueOnly(btcusd, 'USD')
# ar.abdiRanaldoValueOnly(btceur, 'EUR')
# ar.abdiRanaldoValueOnly(btcjpy, 'JPY')
# ar.abdiRanaldoValueOnly(btcgbp, 'GBP')
ar.printStandardisedAr(btcusd, btceur, btcgbp, btcjpy)


# Uncomment this line of code to show the CS, the Amihud and the AR value
# comp.comparison(btcusd, 'USD')
# comp.comparison(btceur, 'EUR')
# comp.comparison(btcjpy, 'JPY')
# comp.comparison(btcgbp, 'GBP')


# Uncomment this line of code to show the detailed AR calculation on the console
# ar.printAbdiRanaldo(btcusd, 'USD')
# ar.printAbdiRanaldo(btceur, 'EUR')
# ar.printAbdiRanaldo(btcjpy, 'JPY')
# ar.printAbdiRanaldo(btcgbp, 'GBP')


# Uncomment this lines of code to show the returns of each BTC-currency pair
# ll.printFullReturns(btcusd, btceur, btcjpy, btcgbp)
# ll.printFullPercentageReturns(btcusd, btceur, btcjpy, btcgbp)
# ll.printReturns(btcusd, btceur, btcjpy, btcgbp)
# ll.printPercentageReturns(btcusd, btceur, btcjpy, btcgbp)


# TODO Ausrei??erwert
# Uncomment this lines of code to plot the returns of BTC currency pairs
#ll.plotDf(btcusd, btceur, btcjpy, btcgbp, 'JPY', 'USD', 'EUR', 'JPY')       #Ausrei??er
#ll.createDataFrame(btcusd, btceur, btcjpy, btcgbp)
#ll.createDataFrameSingeCurrency(btcusd, btceur, btcjpy, btcgbp, 'USD')
#ll.plotOne(btcusd, btceur, btcjpy, btcgbp, 'USD')
#ll.plotOne(btcusd, btceur, btcjpy, btcgbp, 'EUR')
#ll.plotOne(btcusd, btceur, btcjpy, btcgbp, 'GBP')
#ll.plotOne(btcusd, btceur, btcjpy, btcgbp, 'JPY')

#ll.getOutliersIndex(btcusd)
#ll.getDates(ll.getOutliersIndex(btcusd), btcusd)
#ll.getAutocorrelation(btcusd, 'btcusd')
#ll.getAutocorrelation(btceur, 'btceur')
#ll.getAutocorrelation(btcjpy, 'btcjpy')
#ll.getAutocorrelation(btcgbp, 'btcgbp')
