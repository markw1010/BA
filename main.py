import pandas as pd

from AbdiRanaldo import AbdiRanaldo
from Amihud import Amihud
from CorwinSchultz import CorwinSchultz
from Filter import Filter
from RegressionCS import RegressionCS
from RegressionAR import RegressionAR


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

Brauneis, A., Mestel, R., Riordan, R., Theissen, E., 2021. How to measure the liquidi-ty of cryptocurrency markets? 
Journal of Banking and Finance 124 (2021) 106041. 1-26

Author: Mark Wagner
"""

# Prototype dataset
btcusdD = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCUSD_d.csv')
btceurD = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCEUR_d.csv')
btcjpyD = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCJPY_d.csv')
btcgbpD = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/daily/Bitfinex_BTCGBP_d.csv')

# Hourly Data
"""
Amount of standardised data: 34137
"""
btcusdH = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCUSD_1h.csv')
btceurH = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCEUR_1h.csv')
btcjpyH = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCJPY_1h.csv')
btcgbpH = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCGBP_1h.csv')

# Minutely Data
#btcusd = pd.read_csv('/Users/markwagner/Documents/Uni/WS21: 22/BA /Kursdaten/minütlich/Bitfinex_BTCUSD_minute.csv')
#btceur = pd.read_csv('/Users/markwagner/Documents/Uni/WS21: 22/BA /Kursdaten/minütlich/Bitfinex_BTCEUR_minute (1).csv')
#btcgbp = pd.read_csv('/Users/markwagner/Documents/Uni/WS21: 22/BA /Kursdaten/minütlich/Bitfinex_BTCGBP_minute (1).csv')
#btcjpy = pd.read_csv('/Users/markwagner/Documents/Uni/WS21: 22/BA /Kursdaten/minütlich/Bitfinex_BTCJPY_minute (1).csv')

amihud = Amihud()
cs = CorwinSchultz()
ar = AbdiRanaldo()
filter = Filter()
regCS = RegressionCS()
regAR = RegressionAR()

# Uncomment this line of code to show the whole dataset on the console
# filter.print_full(btcusd)
# filter.print_full(btceur)
# filter.print_full(btcjpy)
# filter.print_full(btcgbp)

# Uncomment this lines of code to show the dataset on the console
#print(btcusd)
# print(btceur)
# print(btcjpy)
# print(btcgbp)


# Uncomment this line of code to show the detailed CS calculation on the console
#cs.printCsValues(btcusdH, btceurH, btcgbpH, btcjpyH)
#cs.printAllCsValues(btcusd, btceur, btcgbp, btcjpy)
cs.csGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#cs.getStandardisedCsGroupByDay(btcusdH, btceurH, btcgbpH, btcjpyH)
#cs.showAutocorrGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#cs.crossCorrGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.crossCorrGraphEUR(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.crossCorrGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#cs.getBiggest(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.getBiggest(btcusdH, btceurH, btcgbpH, btcjpyH)
#cs.showAutocorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#cs.autocorrData(btcusdD, btceurD, btcgbpD, btcjpyD)
#cs.getStandardisedCsGroupByDayPercentage(btcusdH, btceurH, btcgbpH, btcjpyH)


# Uncomment this line of code to show the single AR value on the console
#ar.arGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.showAutocorrGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.crossCorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.getBiggest(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.autocorrData(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.calcAutocorrGraphAbs(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.crossCorrGraphMntl(btcusd, btceur, btcgbp, btcjpy)
#ar.showAutocorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)


#regCS.regEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)


#################
# Konkurrent AR #
#################

#regAR.regEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketGbp(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbpJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketJpy(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketJpy(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketUsd(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regUsdEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbpUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regUsdGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdGbp(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regJpyUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regUsdJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdJpy(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regGbpEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbpJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyGbp(btcusdH, btceurH, btcgbpH, btcjpyH)

##############
# Führung AR #
##############

#regAR.regEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regMarketUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsMarketUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regUsdEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbpUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regUsdGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regJpyUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regUsdJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsUsdJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#egAR.regEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regEurGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsEurGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regGbpEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regAR.regGbpJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsGbpJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.regJpyGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.olsJpyGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)


#################
# Konkurrent CS #
#################

#regCS.regEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketGbp(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketJpy(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketUsd(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regUsdEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regGbpUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regUsdGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdGbp(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regJpyUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyUsd(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regUsdJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdJpy(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regGbpEur(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpEur(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regGbpJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpJpy(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regJpyGbp(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyGbp(btcusdH, btceurH, btcgbpH, btcjpyH)

##############
# Führung CS #
##############

#regCS.regEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regMarketUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsMarketUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regUsdEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regGbpUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regUsdGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regJpyUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyUsdLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regUsdJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsUsdJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsEurGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regGbpEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpEurLagged(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regGbpJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsGbpJpyLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.regJpyGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.olsJpyGbpLagged(btcusdH, btceurH, btcgbpH, btcjpyH)





