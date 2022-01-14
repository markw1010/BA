import numpy as np

"""
This class provides all necessary methods and variables to calculate the AR liquidity estimator for a daily, hourly 
or minutely cvs datasets respectively. 

Abdi, F., Ranaldo, A., 2017. A simple estimation of bid-ask spreads from daily close, high, and low prices. The Review 
of Financial Studies, Volume 30, Issue 12, December 2017. 4437-4480
"""


class AbdiRanaldo:

    highStr = []
    lowStr = []
    closeStr = []

    np.highFlt = []
    np.lowFlt = []
    np.closeFlt = []

    """
    This method prints the value for the AR estimator which is referenced at the top of the class description. 
    Therefore it first extract all relevant data in String format, then the data will be saved as floater so that the 
    value for the amihud estimator can be calculated. At the end, the value will be printed on the console

    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the AR estimator as well as other pre calculation values will be printed on the 
                console 
    """
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

    """
    This method prints only the value for the AR estimator on the console.

    Requires:   The cvs file has to be formatted so that it can be read
                The delimiter between the values in the cvs has to be a semicolon

    Ensures:    a floater value for the AR estimator will be printed on the console 
    """
    def abdiRanaldoValueOnly(self, fileReader):
        self.extractStr(fileReader)
        self.extractFlt()
        ARt = self.getARt()

        print('ARt: ')
        print(ARt)

    """
    This method is only implemented for the use of comparison to the AR estimator in the comparison class.
    """
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

    """
    this method returns the value for p_i which ist the addition of hi and li divided by two.
.    
    Requires:   len(hi) = len(li)
    
    Ensures: An array with the pi values will be returned   
    """
    def getPi(self):
        hi = self.getHi()
        li = self.getLi()
        hili = np.add(hi, li)
        pi = np.divide(hili, 2)
        return pi

    """
    This method returns the value of ARi.
    
    Requires:   len(pi1) + len(ci1) >= 4
                term3 >= 0
    
    Ensures:    An array with all ARi values will be returned 
    """
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

    """
    This method calculates and returns the AR_t estimator for interval t which is the average of the AR_t,i measures
    for all adjacent subintervals i in t
    
    Requires:   len(ARi) > 0
    
    Ensures:    A floater value will be returned      
    """
    def getARt(self):
        ARi = self.getARi()
        sum = np.sum(ARi)
        amount = len(ARi)
        ARt = sum/amount
        return ARt