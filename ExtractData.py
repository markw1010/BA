from abc import abstractmethod, ABC


class ExtractData(ABC):

    @abstractmethod
    def extractStr(self):
        pass

    @abstractmethod
    def extractFlt(self):
        pass

    # """
    # Returns from close data
    # """
    # @abstractmethod
    # def extractReturn(self):
    #     pass
