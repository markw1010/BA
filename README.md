# BA
liquidity measures on BTC to other currencies

This programm provides methods and variables in two classes that allows to calculate the liquidity measures of Corwin Schultz (2012) and Amihud (2002) 
for high and low frquency datasets of Bitcoin (BTC).<sup>1</sup> Therefore a cvs document is mandatory with all relevant data which is the high price, low price, open price,
close price and the volume. In this program a dataset of daily data of BTC is already provided from the crypto currency exchange Bitfinex.<sup>2</sup> The user of the program can load the data from any provider, as long as all requirements are ensured. This project is concipated to estimate the liquidity of BTC to other fiat currencies, namely USD, EUR, 
GBP and JPY. The program can also be used to calculate the liquidity of other cryptocurrencies like Etherium (ETH).

* * *
###### <sup>1</sup> Amihud, Y., 2002. *Illiquidity and stock returns: cross-section and time-series effects.* Journal of Financial Markets 5. 31-56 and Corwin, S., Schultz, P., 2012. *A simple way to estimate bid-ask spreads from daily high and low prices.* The Journal of Finance, Volume 67, Issue 2. 719-760

###### <sup>2</sup> Cryptodatadownload *https://www.cryptodatadownload.com/data/bitfinex/* access on 11-21-2021

## Requiremnets
Most of the requirements are fulfilled when the data is downloaded from https://www.cryptodatadownload.com/data/bitfinex/ (11-21-2021). Anyway, in case that the
data is not provided from the recommended website make sure that the following requirements are given:

1. the document is in cvs format
2. delimiter in between the data points is a semicolon (;)
3. Decimial values have to be written the american way. E.g. Pi = 3.141... **(not)** Pi = 3,141...

### Amihud
To calculate the Amihud (AH) illiquidity estimator the dataset must provide the open price, the close price and the traded volume of a cryptocurrency for a specific 
time period. It is also mandatory, that the columns of the needed data are called: 'open', 'close' and 'Volume [currency ticker e.g. Volume USD]'

### Corwin and Schultz
To calculate the Corwin and Schultz (CS) liquidity estimator it is mandatory that the dataset provides high prices and low prices of a cryptocurrency in a specific
time period. The columns of the needed data have to be called: 'high' and 'low'.
