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
#cs.crossCorrGraph(btcusd, btceur, btcgbp, btcjpy)
#cs.crossCorrTable(btcusd, btceur, btcgbp, btcjpy)
#cs.crossCorrData(btcusd, btceur, btcgbp, btcjpy)
#cs.getBiggest(btcusd, btceur, btcgbp, btcjpy)
#cs.autocorrData(btcusd, btceur, btcgbp, btcjpy)


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
#ar.arGraph(btcusd, btceur, btcgbp, btcjpy)
#ar.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy)
#ar.crossCorrGraph(btcusdH, btceurH, btcgbpH, btcjpyH)
#ar.getBiggest(btcusd, btceur, btcgbp, btcjpy)
#ar.autocorrData(btcusd, btceur, btcgbp, btcjpy)
#ar.crossCorrGraphMntl(btcusd, btceur, btcgbp, btcjpy)


#cs.cutCsArray(btcusd, btceur, btcgbp, btcjpy)
#amihud.cutAhArray(btcusd, btceur, btcgbp, btcjpy)
#amihud.getAmihudExpression(btcgbpH, 'GBP')
#amihud.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy)

#cs.printCsValues(btcusdH, btceurH, btcgbpH, btcjpyH)
#reg.marketLiqEURCS(btcusdH, btceurH, btcgbpH, btcjpyH)
#reg.weightedMarketLiqEURCS(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.regEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.olsEurCS(btcusd, btceur, btcgbp, btcjpy)
#regCS.olsGbpCS(btcusd, btceur, btcgbp, btcjpy)
#regCS.olsJpyCS(btcusd, btceur, btcgbp, btcjpy)
#regCS.olsUsdCS(btcusd, btceur, btcgbp, btcjpy)

#regCS.olsMarketEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsMarketGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsMarketJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsMarketUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.tTestEUR(btcusd, btceur, btcgbp, btcjpy)
#regCS.tTestGBP(btcusd, btceur, btcgbp, btcjpy)
#regCS.tTestJPY(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.tTestUSD(btcusd, btceur, btcgbp, btcjpy)

#regCS.histogram(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.regEurAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regGbpAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regJpyAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.regUsdAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsEurAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsGbpAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsJpyAR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.olsUsdAR(btcusdD, btceurD, btcgbpD, btcjpyD)

#regAR.tTestEUR(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.tTestGBP(btcusdD, btceurD, btcgbpD, btcjpyD)
#regAR.tTestJPY(btcusdH, btceurH, btcgbpH, btcjpyH)
#regAR.tTestUSD(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.marketLiqUSDCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.percentageMarketLiqEURCS(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.percentageEURCS(btcusdH, btceurH, btcgbpH, btcjpyH)

#regCS.lRUSD(btcusdH, btceurH, btcgbpH, btcjpyH)
#regCS.round(4.1234567)

#regCS.regEurUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpUsd(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyUsd(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regUsdEur(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdJpy(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regEurJpy(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regEurGbp(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regEurJpy(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regGbpJpy(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.olsEurUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsGbpUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsJpyUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.olsUsdEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsGbpUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsUsdGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsUsdJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.olsJpyEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsEurJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsUsdJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.olsGbpEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsEurGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.olsGbpJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsJpyGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)

regCS.regUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
regCS.olsUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

regCS.regMarketUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
regCS.olsMarketUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

regCS.regEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
regCS.olsEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

regCS.regMarketEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
regCS.olsMarketEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

regCS.regGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)


regCS.regMarketGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)


regCS.regJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)


regCS.regMarketJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)


##############
#regCS.regEurUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsEurUsdLaggedCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsGbpUsdLaggedCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsJpyUsdLaggedCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regGbpEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsGbpEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsUsdEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsEurUsdLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsGbpUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regUsdGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsUsdGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regUsdJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsUsdJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regJpyEurLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsEurJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regEurGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsEurGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regGbpJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsGbpJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regJpyGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.olsJpyGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regEurGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regJpyGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdGbpLagged(btcusdD, btceurD, btcgbpD, btcjpyD)

#regCS.regEurJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regGbpJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regUsdJpyLagged(btcusdD, btceurD, btcgbpD, btcjpyD)
##############

#regCS.regMarketUsdCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regMarketEurCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regMarketGbpCS(btcusdD, btceurD, btcgbpD, btcjpyD)
#regCS.regMarketJpyCS(btcusdD, btceurD, btcgbpD, btcjpyD)