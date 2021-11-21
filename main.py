import csv

from tabulate import tabulate

from Amihud import Amihud
from Comparison import Comparison
from CorwinSchultz import CorwinSchultz
from Filter import Filter

"""
This program will take a cvs file which contains daily, hourly or minutely high and low, open and close as well as other 
data respectively provided by Bitfinex. It will filter and show all the relevant information needed, to calculate the 
liquidity measures of Amihud (2002) and Corwin and Schultz (2012). The Liquidity estimators are inspired by the measures 
which are presented in the following paper:

Amihud, Y., 2002. Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets 5. 
31-56

Corwin, S., Schultz, P., 2012. A simple way to estimate bid-ask spreads from daily 	high and low prices. The Journal of 
Finance, Volume 67, Issue 2. 719-760

Author: Mark Wagner
"""

# Prototype dataset
file = open('Bitfinex_BTCUSD_d_1.csv', newline='')
BTCUSD_csv = csv.DictReader(file, delimiter=';')



amihud = Amihud()
cs = CorwinSchultz()
comp = Comparison()
filter = Filter()

filter.filterCvs(BTCUSD_csv)                      # Uncomment this line of code to show the whole dataset on the console

#amihud.amihudDetailed(BTCUSD_csv)          # Uncomment this line of code to show the amihud calculation on the console

#cs.corwinSchultzDetailed(BTCUSD_csv)       # Uncomment this line of code to show the CS calculation on the console

#amihud.amihudValueOnly(BTCUSD_csv)

#cs.corwinSchultzValueOnly(BTCUSD_csv)

#comp.comparison(BTCUSD_csv)



