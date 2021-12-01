import numpy as np


class AbdiRanaldo:

    highStr = []
    lowStr = []
    closeStr = []

    np.highFlt = []
    np.lowFlt = []
    np.closeFlt = []

    def abdiRanaldoDetailed(self, fileReader):
        self.extractStr(fileReader)
        self.extractFlt()
        self.printAbdiRanaldo()


    def printAbdiRanaldo(self):
        ARt = self.getARt()
        ARi = self.getARi()
        print('ARi: ')
        print(ARi)
        print('--------------')
        print('len(ARi): ')
        print(len(ARi))
        print('--------------')
        print('np.sum(ARi): ')
        print(np.sum(ARi))
        print('--------------')
        print('ARt: ')
        print(ARt)
        print('--------------')

    def abdiRanaldoValueOnly(self, fileReader):
        self.extractStr(fileReader)
        self.extractFlt()
        ARt = self.getARt()

        print('ARt: ')
        print(ARt)

    def abdiRanaldoComparison(self):
        ARt = self.getARt()

        print('ARt: ')
        print(ARt)

    def getHi(self):
        hi = np.log(np.highFlt)
        return hi

    def getLi(self):
        li = np.log(np.lowFlt)
        return li

    def getCi(self):
        ci = np.log(np.closeFlt)
        return ci

    def getPi(self):
        hi = self.getHi()
        li = self.getLi()
        hili = np.add(hi, li)
        pi = np.divide(hili, 2)
        return pi

    def getARi(self):
        ci = self.getCi()
        pi = self.getPi()

        pi1 = np.delete(pi, 0)
        ci1 = np.delete(ci, -1)

        firstPart = np.subtract(ci, pi)
        firstPart = np.delete(firstPart, -1)
        secondPart = np.subtract(ci1, pi1)

        term = np.multiply(firstPart, secondPart)
        term2 = np.multiply(term, 4)
        term3 = np.maximum(term2, 0)

        ARi = np.power(term3, 0.5)

        return ARi

    def getARt(self):
        ARi = self.getARi()
        sum = np.sum(ARi)
        amount = len(ARi)
        ARt = sum/amount
        return ARt

    """
        This method copies the open price, close prise and volume USD amount of the arrays into arrays named np.openFlt,
        np.closeFlt and np.volumeUSDFlt as floater value

        Requires:   all the values in openStr, closeStr and volumeUSDStr should contain only floater values

        Ensures:    all values in openStr, closeStr and volumeUSDStr will be copied in separated arrays as floater values
        """

    # TODO make it work for all types of currencies not only USD!
    def extractFlt(self):
        for value in self.highStr:
            np.highFlt.append(float(value))
        for value in self.lowStr:
            np.lowFlt.append(float(value))
        for value in self.closeStr:
            np.closeFlt.append(float(value))

    """
       This method extract the open prices, close prices and USD volume of a cvs file with daily, hourly or minutely data 
       and safes them as strings in separated arrays called openStr, closeStr and volumeUSDStr. 

       Requires:   The cvs file has to be formatted so that it can be read
                   The columns in the cvs file have to be called 'open', 'close' and 'Volume USD'

       Ensures:    three arrays will be filled with the string representatives of the open price, close price and Volume 
                   USD respectively 
       """

    # TODO make it work for all types of currencies not only USD!
    def extractStr(self, fileReader):
        for item in fileReader:
            self.highStr.append(item['high'])
            self.lowStr.append(item['low'])
            self.closeStr.append(item['close'])
        self.highStr.remove('high')
        self.lowStr.remove('low')
        self.closeStr.remove('close')