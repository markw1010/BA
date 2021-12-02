import csv

from AbdiRanaldo import AbdiRanaldo
from Amihud import Amihud
from Comparison import Comparison
from CorwinSchultz import CorwinSchultz
from Filter import Filter

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
file = open('Bitfinex_BTCUSD_d_1.csv', newline='')
BTCUSD_csv = csv.DictReader(file, delimiter=';')

amihud = Amihud()
cs = CorwinSchultz()
comp = Comparison()
ar = AbdiRanaldo()
filter = Filter()

# Uncomment this line of code to show the whole dataset on the console
#filter.filterCvs(BTCUSD_csv)

# Uncomment this line of code to show the detailed Amihud calculation on the console
#amihud.amihudDetailed(BTCUSD_csv)

# Uncomment this line of code to show the detailed CS calculation on the console
#cs.corwinSchultzDetailed(BTCUSD_csv)

# Uncomment this line of code to show the single Amihud value on the console
#amihud.amihudValueOnly(BTCUSD_csv)

# Uncomment this line of code to show the single CS value on the console
#cs.corwinSchultzValueOnly(BTCUSD_csv)

# Uncomment this line of code to show the single AR value on the console
#ar.abdiRanaldoValueOnly(BTCUSD_csv)

# Uncomment this line of code to show the CS, the Amihud and the AR value
#comp.comparison(BTCUSD_csv)

# Uncomment this line of code to show the detailed AR calculation on the console
ar.abdiRanaldoDetailed(BTCUSD_csv)
