class order:
    def __init__(self):
        self.orderid=''
        self.customerid=''
        self.orderdate=''
        self.totalamount=''

    def setorderid(self,orderid):
        self.orderid=orderid
    def setcustomerid(self,customerid):
        self.customerid=customerid
    def setorderdate(self,orderdate):
        self.orderdate=orderdate
    def settotalamount(self,totalamount):
        self.totalamount=totalamount

    def getorderid(self):
        return self.orderid
    def getcustomerid(self):
        return self.customerid
    def getorderdate(self):
        return self.orderdate
    def gettotalamount(self):
        return self.totalamount