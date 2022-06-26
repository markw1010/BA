import numpy as np
from CorwinSchultz import CorwinSchultz
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm
import scipy.stats as stats

class RegressionCS:

    def marketLiqEURCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCEUR']
        return df

    def marketLiqGBPCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCGBP']
        return df

    def marketLiqJPYCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCJPY']
        return df

    def marketLiqUSDCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)
        del df['BTCUSD']
        return df

    def weightedMarketLiqEURCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        #weightedBtcgbp, weightedBtcjpy, weightedBtcusd, weightedMarketLiq = self.eurShares(fileEUR, fileGBP, fileJPY,
         #                                                                                  fileUSD)

        df = self.marketLiqEURCS(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()
        btcjpy = df['BTCJPY'].to_numpy()

        weightedBtcusd = []
        weightedBtcgbp = []
        weightedBtcjpy = []

        for value in btcusd:
            value = value * 0.89
            weightedBtcusd.append(value)

        for value in btcgbp:
            value = value * 0.06
            weightedBtcgbp.append(value)

        for value in btcjpy:
            value = value * 0.05
            weightedBtcjpy.append(value)

        add1 = [x + y for x, y in zip(weightedBtcusd, weightedBtcgbp)]
        weightedMarketLiq = [x + y for x, y in zip(add1, weightedBtcjpy)]

        return weightedMarketLiq

    def eurSharesCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqEURCS(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()
        btcjpy = df['BTCJPY'].to_numpy()

        weightedBtcusd = []
        weightedBtcgbp = []
        weightedBtcjpy = []
        weightedMarketLiq = []

        for value in btcusd:
            value = value * 0.89
            weightedBtcusd.append(value)

        for value in btcgbp:
            value = value * 0.06
            weightedBtcgbp.append(value)

        for value in btcjpy:
            value = value * 0.05
            weightedBtcjpy.append(value)

        return weightedBtcgbp, weightedBtcjpy, weightedBtcusd, weightedMarketLiq

    def weightedMarketLiqGBPCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        weightedBtceur, weightedBtcjpy, weightedBtcusd, weightedMarketLiq = self.gbpSharesCS(fileEUR, fileGBP, fileJPY,
                                                                                             fileUSD)

        add1 = [x + y for x, y in zip(weightedBtcusd, weightedBtceur)]
        weightedMarketLiq = [x + y for x, y in zip(add1, weightedBtcjpy)]

        return weightedMarketLiq

    def gbpSharesCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btceur = df['BTCEUR'].to_numpy()
        btcjpy = df['BTCJPY'].to_numpy()

        weightedBtcusd = []
        weightedBtceur = []
        weightedBtcjpy = []
        weightedMarketLiq = []

        for value in btcusd:
            value = value * 0.89
            weightedBtcusd.append(value)

        for value in btceur:
            value = value * 0.06
            weightedBtceur.append(value)

        for value in btcjpy:
            value = value * 0.05
            weightedBtcjpy.append(value)

        return weightedBtceur, weightedBtcjpy, weightedBtcusd, weightedMarketLiq

    def weightedMarketLiqJPYCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        weightedBtceur, weightedBtcgbp, weightedBtcusd, weightedMarketLiq = self.jpySharesCS(fileEUR, fileGBP, fileJPY,
                                                                                             fileUSD)

        add1 = [x + y for x, y in zip(weightedBtcusd, weightedBtceur)]
        weightedMarketLiq = [x + y for x, y in zip(add1, weightedBtcgbp)]

        return weightedMarketLiq

    def jpySharesCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()
        btceur = df['BTCEUR'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()

        weightedBtcusd = []
        weightedBtceur = []
        weightedBtcgbp = []
        weightedMarketLiq = []

        for value in btcusd:
            value = value * 0.88
            weightedBtcusd.append(value)

        for value in btceur:
            value = value * 0.06
            weightedBtceur.append(value)

        for value in btcgbp:
            value = value * 0.06
            weightedBtcgbp.append(value)

        return weightedBtceur, weightedBtcgbp, weightedBtcusd, weightedMarketLiq



    def usdSharesCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        df = self.marketLiqUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)

        btcjpy = df['BTCJPY'].to_numpy()
        btceur = df['BTCEUR'].to_numpy()
        btcgbp = df['BTCGBP'].to_numpy()

        weightedBtcjpy = []
        weightedBtceur = []
        weightedBtcgbp = []
        weightedMarketLiq = []

        for value in btcjpy:
            value = value * 0.3
            weightedBtcjpy.append(value)

        for value in btceur:
            value = value * 0.37
            weightedBtceur.append(value)

        for value in btcgbp:
            value = value * 0.33
            weightedBtcgbp.append(value)

        return weightedBtceur, weightedBtcgbp, weightedBtcjpy, weightedMarketLiq


    def percentageEURCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)

        btceur = df['BTCEUR'].to_numpy()

        return btceur

    def percentageGBPCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)

        btcgbp = df['BTCGBP'].to_numpy()

        return btcgbp

    def percentageJPYCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)

        btcjpy = df['BTCJPY'].to_numpy()

        return btcjpy

    def percentageUSDCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        cs = CorwinSchultz()
        df = cs.cutCsArray(fileEUR, fileGBP, fileJPY, fileUSD)

        btcusd = df['BTCUSD'].to_numpy()

        return btcusd

    def weightedMarketLiqUSDCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        weightedBtceur, weightedBtcgbp, weightedBtcjpy, weightedMarketLiq = self.usdSharesCS(fileEUR, fileGBP, fileJPY,
                                                                                             fileUSD)

        add1 = [x + y for x, y in zip(weightedBtcjpy, weightedBtceur)]
        weightedMarketLiq = [x + y for x, y in zip(add1, weightedBtcgbp)]

        return weightedMarketLiq


    def regEurCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEURCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqEURCS(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/EUR Liquidität')
        plt.title('Lineare Regression - BTC/EUR (Corwin und Schultz) [Minütlich]')
        plt.scatter(marketLiq, eurLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, eurLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def olsEurCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEURCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqEURCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(eurLiq, marketLiq).fit()
        print(result.summary())

    def regGbpCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/GBP Liquidität')
        plt.title('Lineare Regression - BTC/GBP (Corwin und Schultz) [Minütlich]')
        plt.scatter(marketLiq, gbpLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, gbpLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def olsGbpCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(gbpLiq, marketLiq).fit()
        print(result.summary())

    def regJpyCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/JPY Liquidität')
        plt.title('Lineare Regression - BTC/JPY (Corwin und Schultz) [Minütlich]')
        plt.scatter(marketLiq, jpyLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, jpyLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def olsJpyCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(jpyLiq, marketLiq).fit()
        print(result.summary())

    def regUsdCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)

        plt.xlabel('Markt Liquidität')
        plt.ylabel('BTC/USD Liquidität')
        plt.title('Lineare Regression - BTC/USD (Corwin und Schultz) [Minütlich]')
        plt.scatter(marketLiq, usdLiq, 7, alpha=0.6, color='blue')
        sb.regplot(marketLiq, usdLiq, ci=None, scatter_kws={"color": "blue", 's':0.5}, line_kws={"color": "red",
                                                                                                 'linewidth':1.5})
        plt.show()

    def olsUsdCS(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = sm.add_constant(marketLiq)
        result = sm.OLS(usdLiq, marketLiq).fit()
        print(result.summary())

    def histogram(self, fileEUR, fileGBP, fileJPY, fileUSD):
        x = self.percentageUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)
        plt.hist(x, bins=10000)
        plt.title('Histogram Marktliqitität (exkl. BTCUSD) - CS')
        plt.show()

    def tTestEUR(self, fileEUR, fileGBP, fileJPY, fileUSD):
        eurLiq = self.percentageEURCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqEURCS(fileEUR, fileGBP, fileJPY, fileUSD)

        meanEur = self.getMean(eurLiq)
        meanMarket = self.getMean(marketLiq)

        eurVar = self.getVar(eurLiq)
        marketVar = self.getVar(marketLiq)

        print('meanEur')
        print(meanEur)
        print('meanMarket')
        print(meanMarket)

        #print('eurVar')
        #print(eurVar)
        #print('marketVar')
        #print(marketVar)

        #print(eurVar/ marketVar)

        ttest = stats.ttest_ind(a=eurLiq, b=marketLiq, equal_var=True)
        print('ttest')
        print(ttest)

    def tTestGBP(self, fileEUR, fileGBP, fileJPY, fileUSD):
        gbpLiq = self.percentageGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqGBPCS(fileEUR, fileGBP, fileJPY, fileUSD)

        meanGbp = self.getMean(gbpLiq)
        meanMarket = self.getMean(marketLiq)

        gbpVar = self.getVar(gbpLiq)
        marketVar = self.getVar(marketLiq)

        print('meanGbp')
        print(meanGbp)
        print('meanMarket')
        print(meanMarket)

        # print('gbpVar')
        # print(gbpVar)
        # print('marketVar')
        # print(marketVar)

        print(gbpVar/ marketVar)

        ttest = stats.ttest_ind(a=gbpLiq, b=marketLiq, equal_var=True)
        print('ttest')
        print(ttest)

    def tTestJPY(self, fileEUR, fileGBP, fileJPY, fileUSD):
        jpyLiq = self.percentageJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqJPYCS(fileEUR, fileGBP, fileJPY, fileUSD)

        meanJpy = self.getMean(jpyLiq)
        meanMarket = self.getMean(marketLiq)

        jpyVar = self.getVar(jpyLiq)
        marketVar = self.getVar(marketLiq)

        print('meanJpy')
        print(meanJpy)
        print('meanMarket')
        print(meanMarket)

        # print('jpyVar')
        # print(jpyVar)
        # print('marketVar')
        # print(marketVar)

        print(jpyVar/ marketVar)

        ttest = stats.ttest_ind(a=jpyLiq, b=marketLiq, equal_var=True)
        print('ttest')
        print(ttest)

    def tTestUSD(self, fileEUR, fileGBP, fileJPY, fileUSD):
        usdLiq = self.percentageUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)
        marketLiq = self.weightedMarketLiqUSDCS(fileEUR, fileGBP, fileJPY, fileUSD)

        meanUsd = self.getMean(usdLiq)
        meanMarket = self.getMean(marketLiq)

        usdVar = self.getVar(usdLiq)
        marketVar = self.getVar(marketLiq)

        print('meanUsd')
        print(meanUsd)
        print('meanMarket')
        print(meanMarket)

        # print('usdVar')
        # print(usdVar)
        # print('marketVar')
        # print(marketVar)

        print(usdVar/ marketVar)

        ttest = stats.ttest_ind(a=usdLiq, b=marketLiq, equal_var=True)
        print('ttest')
        print(ttest)


    def getMean(self, list):
        return sum(list)/len(list)

    def getVar(self, list):
        return np.var(list)