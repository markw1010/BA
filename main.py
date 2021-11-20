import csv

from tabulate import tabulate

from Amihud import Amihud
from CorwinSchultz import CorwinSchultz

"""
This program will take a cvs file which contains daily, hourly or minutely high and low, open and close as well as other 
data respectively provided by Bitfinex. It will filter and show all the relevant information needed, to calculate the 
liquidity measures of Amihud (2002) and Corwin and Schultz (2012). The Liquidity estimators are inspired by the measures 
which are presented in the following paper:

Amihud, Y., 2002. Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets 5. 
31-56

Corwin, S., Schultz, P., 2012. A simple way to estimate bid-ask spreads from daily 	high and low prices. The Journal of 
Finance, Volume 67, Issue 2. 719-760
"""

data = []

file = open('Bitfinex_BTCUSD_d_1.csv', newline='')
# numpy_array = np.loadtxt(file, delimiter=';')

BTCUSD_csv = csv.DictReader(file, delimiter=';')


"""
the method iterates through the data of a cvs file which is formatted by a DictReader and adds all the values into 
an Array called 'data', then it prints the data formatted on the console.

Requires:   cvs files have to be formatted with DictReader
            the values in the cvs file have to be separated by a semicolon

Ensures:    After execution of the method the console will show all data of the cvs file in a formatted way
            all the data will be saved in an array called 'data' as Strings
"""
def filterCvs(fileReader):

    for item in fileReader:
        data.append(item)

    print(tabulate(data))


amihud = Amihud()
cs = CorwinSchultz()

#filterCvs(BTCUSD_csv)
#amihud.getClose(BTCUSD_csv)
#amihud.getClose(BTCUSD_csv)
#amihud.getVolume(BTCUSD_csv, 'USD')
#amihud.amihud(BTCUSD_csv)
cs.corwinSchultz(BTCUSD_csv)
#cs.getLowCS(BTCUSD_csv)
#cs.getGamma()


