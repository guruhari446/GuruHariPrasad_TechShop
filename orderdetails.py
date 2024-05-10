from abc import ABC,abstractmethod

class orderdetails(ABC):
    @abstractmethod
    def CalculateSubtotal(self):
        pass
    @abstractmethod
    def GetOrderDetailInfo(self):
        pass
    @abstractmethod
    def UpdateQuantity(self):
        pass
    @abstractmethod
    def AddDiscount(self):
        pass
