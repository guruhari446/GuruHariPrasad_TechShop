class orderdetail:
    def __init__(self):
        self.orderdetailid = ''
        self.orderid = ''
        self.productid= ''
        self.quantity= ''

    def setorderdetailid (self,orderdetailid ):
        self.orderdetailid =orderdetailid
    def setorderid (self,orderid ):
        self.orderid =orderid
    def setproductid(self,productid):
        self.productid=productid
    def setquantity(self,quantity):
        self.quantity=quantity

    def getorderdetailid (self):
        return self.orderdetailid
    def getorderid (self):
        return self.orderid
    def getproductid(self):
        return self.productid
    def getquantity(self):
        return self.quantity

