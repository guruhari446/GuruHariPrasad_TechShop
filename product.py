class product:
    def __init__(self):
        self.productid=''
        self.productname=''
        self.pdescription=''
        self.price=''

    def setproductid(self,productid):
        self.productid=productid
    def setproductname(self,productname):
        self.productname=productname
    def setpdescription(self,pdescription):
        self.pdescription=pdescription
    def setprice(self,price):
        self.price=price

    def getproductid(self):
        return self.productid
    def getproductname(self):
        return self.productname
    def getpdescription(self):
        return self.pdescription
    def getprice(self):
        return self.price