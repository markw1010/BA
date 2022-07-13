import math

import numpy as np
from CorwinSchultz import CorwinSchultz
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm
import scipy.stats as stats
import pandas as pd
from sklearn.linear_model import LinearRegression

class RegressionCS:

    def marketLiqEUR(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCEUR']
        return df

    def marketLiqGBP(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCGBP']
        return df

    def marketLiqJPY(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCJPY']
        return df

    def marketLiqUSD(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)
        #df.to_excel('/Users/markwagner/Documents/Uni/WS21: 22/BA /Excel/ReferenzdatensatzTäglich.xlsx', index=True)
        del df['BTCUSD']
        return df

    def percentageMarketLiqEUR(self, fileEUR, fileGBP, fileJPY, fileUSD):

        df = self.marketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()
        btcjpy = df['BTCJPY'].to_numpy()
        weightedMarketLiq = []

        add1 = [x + y for x, y in zip(btcusd, btcgbp)]
        MarketLiqSum = [x + y for x, y in zip(add1, btcjpy)]

        for value in MarketLiqSum:
            weighted = value/3
            weightedMarketLiq.append(weighted)

        weightedMarketLiqT = np.delete(weightedMarketLiq, -1)
        weightedMarketLiqT1 = np.delete(weightedMarketLiq, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def percentageMarketLiqGBP(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btceur = df['BTCEUR'].to_numpy()
        btcjpy = df['BTCJPY'].to_numpy()
        weightedMarketLiq = []


        add1 = [x + y for x, y in zip(btcusd, btceur)]
        MarketLiqSum = [x + y for x, y in zip(add1, btcjpy)]

        for value in MarketLiqSum:
            weighted = value/3
            weightedMarketLiq.append(weighted)

        weightedMarketLiqT = np.delete(weightedMarketLiq, -1)
        weightedMarketLiqT1 = np.delete(weightedMarketLiq, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def percentageMarketLiqJPY(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btceur = df['BTCEUR'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()
        weightedMarketLiq = []


        add1 = [x + y for x, y in zip(btcusd, btceur)]
        MarketLiqSum = [x + y for x, y in zip(add1, btcgbp)]

        for value in MarketLiqSum:
            weighted = value/3
            weightedMarketLiq.append(weighted)

        weightedMarketLiqT = np.delete(weightedMarketLiq, -1)
        weightedMarketLiqT1 = np.delete(weightedMarketLiq, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def percentageMarketLiqUSD(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        btcjpy = df['BTCJPY'].to_numpy()
        btceur = df['BTCEUR'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()
        weightedMarketLiq = []

        add1 = [x + y for x, y in zip(btcjpy, btceur)]
        MarketLiqSum = [x + y for x, y in zip(add1, btcgbp)]

        for value in MarketLiqSum:
            weighted = value/3
            weightedMarketLiq.append(weighted)

        weightedMarketLiqT = np.delete(weightedMarketLiq, -1)
        weightedMarketLiqT1 = np.delete(weightedMarketLiq, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage


    def percentageEUR(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)

        btceur = df['BTCEUR'].to_numpy()

        weightedMarketLiqT = np.delete(btceur, -1)
        weightedMarketLiqT1 = np.delete(btceur, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def percentageGBP(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)

        btcgbp = df['BTCGBP'].to_numpy()

        weightedMarketLiqT = np.delete(btcgbp, -1)
        weightedMarketLiqT1 = np.delete(btcgbp, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def percentageJPY(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)

        btcjpy = df['BTCJPY'].to_numpy()

        weightedMarketLiqT = np.delete(btcjpy, -1)
        weightedMarketLiqT1 = np.delete(btcjpy, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def percentageUSD(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.getStandardisedCsGroupByDay(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()

        weightedMarketLiqT = np.delete(btcusd, -1)
        weightedMarketLiqT1 = np.delete(btcusd, 0)

        percentage = [(x / y)-1 for x, y in zip(weightedMarketLiqT1, weightedMarketLiqT)]

        return percentage

    def regEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(marketLiq, eurLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, eurLiq, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(marketLiq, gbpLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, gbpLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def regJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(marketLiq, jpyLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, jpyLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def regUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(marketLiq, usdLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, usdLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def regUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(usdLiq, 0)

        df = pd.DataFrame({'Markt Liquidität': lead,
                           'BTC/USD Liquidität': lag})

        x = df['Markt Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regMarketUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(marketLiq, 0)

        df = pd.DataFrame({'BTC/USD Liquidität': lead,
                           'Markt Liquidität': lag})

        x = df['BTC/USD Liquidität']
        y = df['Markt Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(eurLiq, 0)

        df = pd.DataFrame({'Markt Liquidität': lead,
                           'BTC/EUR Liquidität': lag})

        x = df['Markt Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regMarketEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(marketLiq, 0)

        df = pd.DataFrame({'BTC/EUR Liquidität': lead,
                           'Markt Liquidität': lag})

        x = df['BTC/EUR Liquidität']
        y = df['Markt Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(jpyLiq, 0)

        df = pd.DataFrame({'Markt Liquidität': lead,
                           'BTC/JPY Liquidität': lag})

        x = df['Markt Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regMarketJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(marketLiq, 0)

        df = pd.DataFrame({'BTC/JPY Liquidität': lead,
                           'Markt Liquidität': lag})

        x = df['BTC/JPY Liquidität']
        y = df['Markt Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(gbpLiq, 0)

        df = pd.DataFrame({'Markt Liquidität': lead,
                           'BTC/GBP Liquidität': lag})

        x = df['Markt Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()

    def regMarketGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(marketLiq, 0)

        df = pd.DataFrame({'BTC/GBP Liquidität': lead,
                           'Markt Liquidität': lag})

        x = df['BTC/GBP Liquidität']
        y = df['Markt Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's': 0.5},
                   line_kws={"color": "red", 'linewidth': 1.5})
        plt.show()


    def regMarketUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(usdLiq, marketLiq, 7, alpha=0.6, color='blue')
        sb.regplot(usdLiq, marketLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def regMarketEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(eurLiq, marketLiq, 7, alpha=0.6, color='blue')
        sb.regplot(eurLiq, marketLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def regMarketGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(gbpLiq, marketLiq, 7, alpha=0.6, color='blue')
        sb.regplot(gbpLiq, marketLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def regMarketJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('Markt Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(jpyLiq, marketLiq, 7, alpha=0.6, color='blue')
        sb.regplot(jpyLiq, marketLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def olsGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(gbpLiq, marketLiq).fit()
        print(result.summary())

    def olsMarketGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        gbp = sm.add_constant(gbpLiq)
        result = sm.OLS(marketLiq, gbp).fit()
        print(result.summary())

    def olsJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(jpyLiq, marketLiq).fit()
        print(result.summary())

    def olsMarketJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        jpy = sm.add_constant(jpyLiq)
        result = sm.OLS(marketLiq, jpy).fit()
        print(result.summary())

    def olsUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(usdLiq, marketLiq).fit()
        print(result.summary())

    def olsMarketUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        usd = sm.add_constant(usdLiq)
        result = sm.OLS(marketLiq, usd).fit()
        print(result.summary())

    def olsEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(eurLiq, marketLiq).fit()
        print(result.summary())

    def olsMarketEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        eur = sm.add_constant(eurLiq)
        result = sm.OLS(marketLiq, eur).fit()
        print(result.summary())


    def regEurUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/USD Liquidität': usdLiq,
                            'BTC/EUR Liquidität': eurLiq})

        #trimEur = eurLiq[0:3957]
        #trimMarket = marketLiq[0:3957]

        #df_filtered = df[df['BTC/EUR Liquidität'] < 1000]

        x = df['BTC/USD Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/USD Liquidität': usdLiq,
                            'BTC/EUR Liquidität': eurLiq})

        #trimEur = eurLiq[0:3957]
        #trimMarket = marketLiq[0:3957]

        #df_filtered = df[df['BTC/EUR Liquidität'] < 1000]

        y = df['BTC/USD Liquidität']
        x = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbpUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/USD Liquidität': usdLiq,
                            'BTC/GBP Liquidität': gbpLiq})

        x = df['BTC/USD Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/GBP Liquidität': gbpLiq,
                            'BTC/USD Liquidität': usdLiq})

        x = df['BTC/GBP Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/GBP Liquidität': gbpLiq,
                            'BTC/USD Liquidität': usdLiq})

        x = df['BTC/GBP Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regJpyUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/USD Liquidität': usdLiq,
                            'BTC/JPY Liquidität': jpyLiq})

        x = df['BTC/USD Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/JPY Liquidität': jpyLiq,
                            'BTC/USD Liquidität': usdLiq})

        x = df['BTC/JPY Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regEurJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/JPY Liquidität': jpyLiq,
                           'BTC/EUR Liquidität': eurLiq})

        #trimEur = eurLiq[0:3957]
        #trimMarket = marketLiq[0:3957]

        #df_filtered = df[df['BTC/EUR Liquidität'] < 1000]

        x = df['BTC/JPY Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regJpyEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/EUR Liquidität': eurLiq,
                            'BTC/JPY Liquidität': jpyLiq})

        #trimEur = eurLiq[0:3957]
        #trimMarket = marketLiq[0:3957]

        #df_filtered = df[df['BTC/EUR Liquidität'] < 1000]

        x = df['BTC/EUR Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regEurGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/GBP Liquidität': gbpLiq,
                           'BTC/EUR Liquidität': eurLiq})

        x = df['BTC/GBP Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbpEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/EUR Liquidität': eurLiq,
                            'BTC/GBP Liquidität': gbpLiq})

        x = df['BTC/EUR Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbpJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/JPY Liquidität': jpyLiq,
                            'BTC/GBP Liquidität': gbpLiq})

        x = df['BTC/JPY Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()


    def regJpyGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        df = pd.DataFrame({'BTC/GBP Liquidität': gbpLiq,
                            'BTC/JPY Liquidität': jpyLiq})

        x = df['BTC/GBP Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()


    def olsGbpUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        usd = sm.add_constant(usdLiq)
        result = sm.OLS(gbpLiq, usd).fit()
        print(result.summary())

    def olsUsdGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        gbp = sm.add_constant(gbpLiq)
        result = sm.OLS(usdLiq, gbp).fit()
        print(result.summary())

    def olsJpyUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        usd = sm.add_constant(usdLiq)
        result = sm.OLS(jpyLiq, usd).fit()
        print(result.summary())

    def olsUsdJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        jpy = sm.add_constant(jpyLiq)
        result = sm.OLS(usdLiq, jpy).fit()
        print(result.summary())

    def olsEurUsd(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        usd = sm.add_constant(usdLiq)
        result = sm.OLS(eurLiq, usd).fit()
        print(result.summary())

    def olsUsdEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        eur = sm.add_constant(eurLiq)
        result = sm.OLS(usdLiq, eur).fit()
        print(result.summary())

    def olsEurJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        jpy = sm.add_constant(jpyLiq)
        result = sm.OLS(eurLiq, jpy).fit()
        print(result.summary())

    def olsJpyEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eur = sm.add_constant(eurLiq)
        result = sm.OLS(jpyLiq, eur).fit()
        print(result.summary())

    def olsGbpEur(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eur = sm.add_constant(eurLiq)
        result = sm.OLS(gbpLiq, eur).fit()
        print(result.summary())

    def olsEurGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        gbp = sm.add_constant(gbpLiq)
        result = sm.OLS(eurLiq, gbp).fit()
        print(result.summary())

    def olsGbpJpy(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        jpy = sm.add_constant(jpyLiq)
        result = sm.OLS(gbpLiq, jpy).fit()
        print(result.summary())

    def olsJpyGbp(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        gbp = sm.add_constant(gbpLiq)
        result = sm.OLS(jpyLiq, gbp).fit()
        print(result.summary())

    def regEurUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(eurLiq, 0)


        df = pd.DataFrame({'BTC/USD Liquidität': lead,
                            'BTC/EUR Liquidität': lag})


        x = df['BTC/USD Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbpUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(gbpLiq, 0)


        df = pd.DataFrame({'BTC/USD Liquidität': lead,
                            'BTC/GBP Liquidität': lag})


        x = df['BTC/USD Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(usdLiq, 0)


        df = pd.DataFrame({'BTC/GBP Liquidität': lead,
                            'BTC/USD Liquidität': lag})


        x = df['BTC/GBP Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regJpyUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(jpyLiq, 0)


        df = pd.DataFrame({'BTC/USD Liquidität': lead,
                            'BTC/JPY Liquidität': lag})


        x = df['BTC/USD Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(usdLiq, 0)


        df = pd.DataFrame({'BTC/JPY Liquidität': lead,
                            'BTC/USD Liquidität': lag})


        x = df['BTC/JPY Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbpEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(gbpLiq, 0)


        df = pd.DataFrame({'BTC/EUR Liquidität': lead,
                            'BTC/GBP Liquidität': lag})


        x = df['BTC/EUR Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regEurGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(eurLiq, 0)


        df = pd.DataFrame({'BTC/GBP Liquidität': lead,
                            'BTC/EUR Liquidität': lag})


        x = df['BTC/GBP Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regJpyEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(jpyLiq, 0)


        df = pd.DataFrame({'BTC/EUR Liquidität': lead,
                            'BTC/JPY Liquidität': lag})


        x = df['BTC/EUR Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regEurJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(eurLiq, 0)


        df = pd.DataFrame({'BTC/JPY Liquidität': lead,
                            'BTC/EUR Liquidität': lag})


        x = df['BTC/JPY Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regJpyGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(jpyLiq, 0)


        df = pd.DataFrame({'BTC/GBP Liquidität': lead,
                            'BTC/JPY Liquidität': lag})


        x = df['BTC/GBP Liquidität']
        y = df['BTC/JPY Liquidität']

        plt.xlabel('BTC/GBP Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regGbpJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(gbpLiq, 0)


        df = pd.DataFrame({'BTC/JPY Liquidität': lead,
                            'BTC/GBP Liquidität': lag})


        x = df['BTC/JPY Liquidität']
        y = df['BTC/GBP Liquidität']

        plt.xlabel('BTC/JPY Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regUsdEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(usdLiq, 0)


        df = pd.DataFrame({'BTC/EUR Liquidität': lead,
                            'BTC/USD Liquidität': lag})


        x = df['BTC/EUR Liquidität']
        y = df['BTC/USD Liquidität']

        plt.xlabel('BTC/EUR Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def regEurUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(eurLiq, 0)


        df = pd.DataFrame({'BTC/USD Liquidität': lead,
                            'BTC/EUR Liquidität': lag})


        x = df['BTC/USD Liquidität']
        y = df['BTC/EUR Liquidität']

        plt.xlabel('BTC/USD Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression - Zeitverzögert (Corwin und Schultz) [Täglich]')
        plt.scatter(x, y, 7, alpha=0.6, color='blue')
        sb.regplot(x, y, ci=None, scatter_kws={"color": "blue", 's':0.5},
                                                                            line_kws={"color": "red", 'linewidth':1.5})
        plt.show()

    def olsGbpUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(gbpLiq, 0)

        usd = sm.add_constant(lead)
        result = sm.OLS(lag, usd).fit()
        print(result.summary())

    def olsUsdGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(usdLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())

    def olsJpyUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(jpyLiq, 0)

        usd = sm.add_constant(lead)
        result = sm.OLS(lag, usd).fit()
        print(result.summary())

    def olsUsdJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(usdLiq, 0)

        jpy = sm.add_constant(lead)
        result = sm.OLS(lag, jpy).fit()
        print(result.summary())

    def olsGbpEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(gbpLiq, 0)

        usd = sm.add_constant(lead)
        result = sm.OLS(lag, usd).fit()
        print(result.summary())

    def olsEurGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(eurLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())

    def olsJpyEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(jpyLiq, 0)

        eur = sm.add_constant(lead)
        result = sm.OLS(lag, eur).fit()
        print(result.summary())

    def olsEurJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(eurLiq, 0)

        jpy = sm.add_constant(lead)
        result = sm.OLS(lag, jpy).fit()
        print(result.summary())

    def olsUsdEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(usdLiq, 0)

        eur = sm.add_constant(lead)
        result = sm.OLS(lag, eur).fit()
        print(result.summary())

    def olsEurUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(eurLiq, 0)

        usd = sm.add_constant(lead)
        result = sm.OLS(lag, usd).fit()
        print(result.summary())

    def olsGbpJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(gbpLiq, 0)

        jpy = sm.add_constant(lead)
        result = sm.OLS(lag, jpy).fit()
        print(result.summary())

    def olsJpyGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(jpyLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())

    def olsGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(gbpLiq, 0)

        market = sm.add_constant(lead)
        result = sm.OLS(lag, market).fit()
        print(result.summary())

    def olsMarketGbpLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBP(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqGBP(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(gbpLiq, -1)
        lag = np.delete(marketLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())

    def olsEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(eurLiq, 0)

        market = sm.add_constant(lead)
        result = sm.OLS(lag, market).fit()
        print(result.summary())

    def olsMarketEurLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEUR(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqEUR(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(eurLiq, -1)
        lag = np.delete(marketLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())

    def olsJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(jpyLiq, 0)

        market = sm.add_constant(lead)
        result = sm.OLS(lag, market).fit()
        print(result.summary())

    def olsMarketJpyLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPY(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqJPY(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(jpyLiq, -1)
        lag = np.delete(marketLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())

    def olsUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(marketLiq, -1)
        lag = np.delete(usdLiq, 0)

        market = sm.add_constant(lead)
        result = sm.OLS(lag, market).fit()
        print(result.summary())

    def olsMarketUsdLagged(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSD(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.percentageMarketLiqUSD(fileEUR, fileGBP, fileJPY, fileUSD)

        lead = np.delete(usdLiq, -1)
        lag = np.delete(marketLiq, 0)

        gbp = sm.add_constant(lead)
        result = sm.OLS(lag, gbp).fit()
        print(result.summary())
