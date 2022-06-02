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
btcusd = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCUSD_1h.csv')
btceur = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCEUR_1h.csv')
btcjpy = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCJPY_1h.csv')
btcgbp = pd.read_csv('/Users/markwagner/PycharmProjects/BA/DataSets/hourly/Bitfinex_BTCGBP_1h.csv')

amihud = Amihud()
cs = CorwinSchultz()
comp = Comparison()
ar = AbdiRanaldo()
filter = Filter()
ll = LeadLag()

# Uncomment this line of code to show the whole dataset on the console
# filter.print_full(btcusd)
# filter.print_full(btceur)
# filter.print_full(btcjpy)
# filter.print_full(btcgbp)

# Uncomment this lines of code to show the dataset on the console
# print(btcusd)
# print(btceur)
# print(btcjpy)
# print(btcgbp)


# Uncomment this line of code to show the detailed CS calculation on the console
# cs.printCsValues(btcusd, btceur, btcgbp, btcjpy)
# cs.printAllCsValues(btcusd, btceur, btcgbp, btcjpy)
# cs.csGraph(btcusd, btceur, btcgbp, btcjpy)
#cs.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy)
# cs.getCrossCorrelation(3, btcusd, btceur, btcgbp, btcjpy, 101)
#cs.crossCorrGraph(btcusd, btceur, btcgbp, btcjpy)
#cs.crossCorrTable(btcusd, btceur, btcgbp, btcjpy)
#cs.crossCorrData(btcusd, btceur, btcgbp, btcjpy)
#cs.getBiggest(btcusd, btceur, btcgbp, btcjpy)
#cs.autocorrData(btcusd, btceur, btcgbp, btcjpy)



# TODO JPY values checking
# Uncomment this line of code to show the single Amihud value on the console
# amihud.printStandardisedAh(btcusd, btceur, btcgbp, btcjpy)
# amihud.amihudGraph(btcusd, btceur, btcgbp, btcjpy, 3)
# amihud.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy, 3)


# Uncomment this line of code to show the single AR value on the console
#ar.arGraph(btcusd, btceur, btcgbp, btcjpy, 3)
#ar.showAutocorrGraph(btcusd, btceur, btcgbp, btcjpy)
ar.crossCorrGraph(btcusd, btceur, btcgbp, btcjpy)
#ar.getBiggest(btcusd, btceur, btcgbp, btcjpy)
#ar.autocorrData(btcusd, btceur, btcgbp, btcjpy)
#ar.cutArArray(btcusd, btceur, btcgbp, btcjpy)
#ar.getSmallest(btcusd, btceur, btcgbp, btcjpy)
#ar.getARi(btcgbp)
#ar.mergeARiTupel(btcusd)


# Uncomment this line of code to show the CS, the Amihud and the AR value
# comp.comparison(btcusd, 'USD')
# comp.comparison(btceur, 'EUR')
# comp.comparison(btcjpy, 'JPY')
# comp.comparison(btcgbp, 'GBP')

