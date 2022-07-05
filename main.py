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
# cs.printCsValues(btcusd, btceur, btcgbp, btcjpy)
# cs.printAllCsValues(btcusd, btceur, btcgbp, btcjpy)
#cs.csGraph(btcusd, btceur, btcgbp, btcjpy)
#cs.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy)
#cs.crossCorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#cs.crossCorrTable(btcusd, btceur, btcgbp, btcjpy)
#cs.crossCorrData(btcusd, btceur, btcgbp, btcjpy)
#cs.getBiggest(btcusdD, btceurD, btcgbpD, btcjpyD)
#cs.showAutocorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#cs.autocorrData(btcusdD, btceurD, btcgbpD, btcjpyD)


# TODO JPY values checking
# Uncomment this line of code to show the single Amihud value on the console
# amihud.printStandardisedAh(btcusd, btceur, btcgbp, btcjpy)
#amihud.amihudGraph(btcusd, btceur, btcgbp, btcjpy)
# amihud.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy, 3)
#amihud.crossCorrGraph(btcusd, btceur, btcgbp, btcjpy)
#amihud.getBiggest(btcusd, btceur, btcgbp, btcjpy)
#amihud.autocorrData(btcusd, btceur, btcgbp, btcjpy)
#amihud.showAutocorrGraph(btcgbp, btceur, btcjpy)
#amihud.cutAhArray(btcusd, btceur, btcgbp, btcjpy)


# Uncomment this line of code to show the single AR value on the console
#ar.arGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.showAutocorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.crossCorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.getBiggest(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.autocorrData(btcusdD, btceurD, btcgbpD, btcjpyD)
#ar.crossCorrGraphMntl(btcusd, btceur, btcgbp, btcjpy)
#ar.showAutocorrGraph(btcusdD, btceurD, btcgbpD, btcjpyD)


#regCS.regEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)


##############
# Konkurrent #
##############

#regAR.regEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketEur(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketGbp(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketJpy(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketUsd(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdEur(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regGbpUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdGbp(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regJpyUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdJpy(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyEur(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyEur(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regGbpEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpEur(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regGbpJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyGbp(btcusdD, btceurD, btcgbpD, btcjpyD)

###########
# Führung #
###########

#regAR.regEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regMarketUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsMarketUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regGbpUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regJpyUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regGbpEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regGbpJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)


#regCS.regEurUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)


ar.getStandardisedArGroupByDay(btcusdH, btceurH, btcgbpH, btcjpyH)


