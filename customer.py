class customer:
    def __init__(self):
        self.customerid=''
        self.firstname=''
        self.lastname=''
        self.email=''
        self.phone=''
        self.address=''

    def setcustomerid(self,customerid):
        self.customerid=customerid
    def setfirstname(self,firstname):
        self.firstname=firstname
    def setlastname(self,lastname):
        self.lastname=lastname
    def setemail(self,email):
        self.email=email
    def setphone(self,phone):
        self.phone=phone
    def setaddress(self,address):
        self.address=address

    def getcustomerid(self):
        return self.customerid
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    def getemail(self):
        return self.email
    def getphone(self):
        return self.phone
    def getaddress(self):
        return self.address