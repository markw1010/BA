import csv

from Amihud import Amihud

file = open('Bitfinex_BTCUSD_d_1.csv', newline='')
# numpy_array = np.loadtxt(file, delimiter=';')

BTCUSD_csv = csv.DictReader(file, delimiter=';')

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




def calculateCS():

    #getAlphsCS()

    getBetaCS()

    #getGammaCS()


def getBetaCS():

    getHighCS()

    #getLowCS()


"""
This method returns an array with the close prices of BTC in a specific time period

Requires:   the column with the data for the close prices has to be called 'close' in the cvs file
            The cvs file has to be formatted so that it can be readed
            The delimiter between the values in the cvs has to be a semicolon

Ensures:    An Array will be returned with all the close data represented as Strings
"""
def getHighCS(fileReader):

    high = []

    for item in fileReader:
        high.append(item['high'])

    # print(*values, sep='\n')
    print(high)

    return high


amihud = Amihud()
#amihud.filterCvs(BTCUSD_csv)
#amihud.getClose(BTCUSD_csv)
#amihud.getClose(BTCUSD_csv)
#amihud.getVolume(BTCUSD_csv, 'USD')
amihud.amihud(BTCUSD_csv)



