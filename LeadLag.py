import csv

import numpy as np

class LeadLag():

    returnUSD = []
    returnEUR = []
    returnJPY = []
    returnGBP = []

    closeUSDstr = []
    closeEURstr = []
    closeJPYstr = []
    closeGBPstr = []

    np.closeUSDflt = []
    np.closeEURflt = []
    np.closeJPYflt = []
    np.closeGBPflt = []

    def extractUSDstr(self, fileReader):
        for item in fileReader:
            self.closeUSDstr.append(item['close'])
        self.closeUSDstr.remove('close')

    def extractEURstr(self, fileReader):
        for item in fileReader:
            self.closeEURstr.append(item['close'])
        self.closeEURstr.remove('close')

    def extractJPYstr(self, fileReader):
        for item in fileReader:
            self.closeJPYstr.append(item['close'])
        self.closeJPYstr.remove('close')

    def extractGBPstr(self, fileReader):
        for item in fileReader:
            self.closeGBPstr.append(item['close'])
        self.closeGBPstr.remove('close')

    def extractUSDflt(self):
        for value in self.closeUSDstr:
            np.closeUSDflt.append(float(value))

        print(np.closeUSDflt)

    def extractEURflt(self):
        for value in self.closeEURstr:
            np.closeEURflt.append(float(value))

    def extractJPYflt(self):
        for value in self.closeJPYstr:
            np.closeJPYflt.append(float(value))

    def extractGBPflt(self):
        for value in self.closeGBPstr:
            np.closeGBPflt.append(float(value))


    def extractReturn(self, fileReaderUSD, fileReaderEUR, fileReaderJPY, fileReaderGBP):
        self.extractUSDstr(fileReaderUSD)
        self.extractEURstr(fileReaderEUR)
        self.extractJPYstr(fileReaderJPY)
        self.extractGBPstr(fileReaderGBP)
        closeUSD = self.extractUSDflt()
        closeEUR = self.extractEURflt()
        closeJPY = self.extractJPYflt()
        closeGBP = self.extractGBPflt()
        print(closeUSD)


