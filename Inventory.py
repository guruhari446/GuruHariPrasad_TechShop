class Inventory:
    def __init__(self):
        self.inventoryid = ''
        self.productid = ''
        self.quantityinstock= ''
        self.laststockupdate= ''

    def setinventoryid (self, inventoryid ):
        self.inventoryid  = inventoryid

    def setproductid (self, productid ):
        self.productid = productid

    def setquantityinstock(self, quantityinstock):
        self.quantityinstock = quantityinstock

    def setlaststockupdate(self, laststockupdate):
        self.laststockupdate = laststockupdate

    def getinventoryid (self):
        return self.inventoryid

    def getproductid (self):
        return self.productid

    def getquantityinstock(self):
        return self.quantityinstock

    def getlaststockupdate(self):
        return self.laststockupdate