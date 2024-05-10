import mysql.connector as sql
from Assignment import dao

class implement:
    def open(self):
        try:
            self.conn = sql.connect(host='localhost', database='Assignment', user='root', password='guruhari2002#')
            if self.conn.is_connected:
                print('Database is Connected:')
            else:
                print('Not Connected with Database')
            self.stmt = self.conn.cursor()
            return True
        except Exception as e:
            print(f'Rasied DataBaseConnection:{e}')
            return False

    def close(self):
        self.conn.close()

    def calculateTotalOrders(self):
        try:
            self.open()
            customerid=int(input('Enter the customerid:'))
            select_str='''select orderid from order where customerid=%s'''
            self.stmt.execute(select_str,(customerid,))
            recods=self.stmt.fetchall()
            print('')
            print('__________________Total Orders in Customer Table__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def GetCustomerDetails(self):
        try:
            self.open()
            customerid=int(input('Enter the customerid:'))
            select_str='''select * from customer where customerid=%s'''
            self.stmt.execute(select_str,(customerid,))
            recods=self.stmt.fetchall()
            print('')
            print('__________________Records In Customers Table__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def UpdateCustomerInfo(self):
        try:

            self.customerid = int(input('Enter customerid:'))
            self.firstname = input('Enter firstname:')
            self.lastname = input('Enter lastname:')
            self.email = input('Enter email:')
            self.address = input('Enter address:')
            update_str = 'update customer set firstname =%s,lastname =%s,email = %s,address =%s where customerid=%s'
            self.open()

            data = (self.firstname, self.lastname, self.email,  self.address,self.customerid)

            self.stmt.executemany(update_str,(data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated successfully...')
            return True
        except Exception as e:
            print(f'Raised Invalid Input ;{e}')
            return False

    def GetProductDetails(self):
        try:
            self.open()
            productid=int(input('Enter the productid:'))
            select_str = '''select * from product where productid=%s'''
            self.stmt.execute(select_str,(productid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________Records In Products Table__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def UpdateProductInfo(self):
        try:
            self.productid =int(input('Enter the productid:'))
            self.productname =input('Enter Product Name:')
            self.pdescription =input('Enter the Description:')
            self.price = input('Enter the price:')
            update_str='update product set productname=%s,pdescription=%s,price=%s where productid=%s'
            self.open()
            data=(self.productid,self.productname,self.pdescription,self.price)
            self.stmt.executemany(update_str, (data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated successfully...')
            return True
        except Exception as e:
            print(f'Raised Invalid Input ;{e}')
            return False

    def IsProductStock(self):
        try:
            self.open()
            productid=int(input('Enter the productid:'))
            select_str = '''select quantityinstock from Inventory where productid=%s '''
            self.stmt.execute(select_str,(productid,))
            recods = self.stmt.fetchall()
            print('')
            print('__________________Products checked in Products Table__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def CalculateTotalAmount(self):
        try:
            self.open()
            orderid=int(input('Enter the orderid:'))
            select_str = '''select totalamount from order where orderid=%s '''
            self.stmt.execute(select_str,(orderid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________Total amount calculated from orders__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def GetOrderDetails(self):
        try:
            self.open()
            orderid=int(input('Enter the orderid: '))
            select_str = '''select p.product,or.quantity from product p join orderdetail or on p.productid=or.productid join order o on o.orderid=or.orderid '''
            self.stmt.execute(select_str,(orderid,))
            recods = self.stmt.fetchall()
            print('')
            print('__________________Order Details are retrived__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def UpdateOrderStatus(self):
        try:
            self.orderid = int(input('Enter the orderid:'))
            self.customerid = int(input('Enter the customerid:'))
            self.orderdate = input('Enter the order date:')
            self.totalamount = int(input('Enter the Total amount:'))
            update_str = 'update order set customerid=%s,orderdate=%s,totalamount=%s  where orderid=%s'
            self.open()
            data = (self.customerid,self.orderdate,self.totalamount,self.orderid)
            self.stmt.executemany(update_str, (data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated successfully...')
            return True

        except Exception as e:
            print(f'Raised Invalid Input ;{e}')
            return False

    def CancelOrder(self):
        try:
            orderid = int(input('enter the orderid to be deleted:'))
            delete_str = 'delete from order where orderid=%s'
            self.open()
            self.stmt.execute(delete_str, (orderid,))
            self.conn.commit()
            print('Records Deleted Successfully--------')
            return True
        except Exception as e:
            print(f'Raised Invalid Input :{e}')
            return False

    def CalculateSubTotal(self):
        try:
            self.open()
            orderid=int(input('Enter the orderid:'))
            select_str = '''select sum(o.totalamount),o.orderdate from order o  join orderdetails or on o.orderid=or.orderid group by o.orderdate'''
            self.stmt.execute(select_str,(orderid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________SubTotal in orderdetailsTable__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def GetOrderDetailInfo(self):
        try:
            self.open()
            orderid=int(input('Enter the orderid:'))
            select_str = '''select * from orderdetails where orderid=%s'''
            self.stmt.execute(select_str,(orderid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________Order Details are retrived__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def UpdateQuantity(self):
        try:
            self.orderdetailid = int(input('Enter the orderdetails:'))
            self.orderid = int(input('Enter the orderid:'))
            self.productid = int(input('Enter the productid:'))
            self.quantity = int(input('Enter the quantity:'))
            update_str = 'update orderdetails set orderid=%s,productid=%s,quantity=%s  where orderdetailid=%s'
            self.open()
            data = (self.customerid, self.orderdate, self.totalamount, self.orderid)
            self.stmt.executemany(update_str, (data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated successfully...')
            return True

        except Exception as e:
            print(f'Raised Invalid Input ;{e}')
            return False

    def GetProduct(self):
        try:
            self.open()
            productid=int(input('Enter the productid:'))
            select_str = '''select p.productname from product p join Inventory i on p.productid=i.productid'''
            self.stmt.execute(select_str,(productid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________Products details are retrived__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def QuantityInStock(self):
        try:
            self.open()
            inventoryid=int(input('Enter the inventoryid:'))
            select_str = '''select quantityinstock from Inventory where inventoryid=%s'''
            self.stmt.execute(select_str,(inventoryid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________quantityinstocks Details are retrived__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

    def AddToInventory(self):
        try:
            self.inventoryid = int(input('Enter the inventoryid:'))
            self.productid = int(input('Enter the productid: '))
            self.quantityinstock = int(input('Enter the quantity in stock:'))
            self.laststockupdate =int(input('Enter the lastStockupdate'))
            print(self.inventoryid, self.productid, self.quantityinstock, self.laststockupdate)

            data = (self.inventoryid, self.productid, self.quantityinstock, self.laststockupdate)
            insert_str = '''insert into Inventory(inventoryid,productid,quantityinstock,laststockupdate)
                                      values(%s,%s,%s,%s)'''
            self.open()
            self.stmt.executemany(insert_str, (data,))
            self.conn.commit()
            print('Records Inserted Successfully..')
            self.close()
            return True

        except Exception as e:
            print(f'Invalid Input:{e}')
            return False

    def RemovefromInventory(self):
        try:

            inventoryid = int(input('enter the inventoryid to be deleted:'))
            delete_str = 'delete from Inventory where inventoryid=%s'
            self.open()
            self.stmt.execute(delete_str, (inventoryid,))
            self.conn.commit()
            print('Records Deleted Successfully--------')
            return True
        except Exception as e:
            print(f'Raised Invalid Input :{e}')
            return False

    def UpdateStockQuantity(self):
        try:

            self.inventoryid = int(input('Enter the inventoryid:'))
            self.productid = int(input('Enter the productid: '))
            self.quantityinstock = int(input('Enter the quantity in stock:'))
            self.laststockupdate =int(input('Enter the lastStockupdate'))
            update_str = 'update Inventory set productid=%s,quantityinstock=%s,laststockupdate=%s  where inventoryid=%s'
            self.open()
            data = (self.inventoryid,self.productid,self.quantityinstock ,self.laststockupdate)
            self.stmt.executemany(update_str, (data,))
            self.conn.commit()
            print(update_str, data)
            print('Records updated successfully...')
            return True

        except Exception as e:
            print(f'Raised Invalid Input ;{e}')
            return False

    def IsProductAvailable(self):
        try:
            self.open()
            inventoryid=int(input('Enter the inventoryid:'))
            select_str = '''select productid from Inventory where inventoryid=%s'''
            self.stmt.execute(select_str,(inventoryid,) )
            recods = self.stmt.fetchall()
            print('')
            print('__________________productid Details are retrived__________')
            for i in recods:
                print(i)
            self.close()
            return True
        except Exception as e:
            print(f"Raised Invalid Input:{e}")
            return False

















