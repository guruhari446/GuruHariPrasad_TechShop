from Assignment.dao.implement import implement
class main:
    def __init__(self):
        self.use=implement()
    def run(self):
        while True:
            print("Techshop Application Menu")
            print("1.calculateTotalOrders")
            print("2.GetCustomerDetails")
            print("3.UpdateCustomerInfo")
            print("4.GetProductDetails")
            print("5.UpdateProductInfo")
            print("6.IsProductStock")
            print("7.CalculateTotalAmount")
            print("8.GetOrderDetails")
            print("9.UpdateOrderStatus")
            print("10.CancelOrder")
            print("11.CalculateSubTotal")
            print("12.GetOrderDetailInfo")
            print("13.UpdateQuantity")
            print("14.GetProduct")
            print("15.QuantityInStock")
            print("16.AddToInventory")
            print("17.RemovefromInventory")
            print("18.UpdateStockQuantity")
            print("19.IsProductAvailable")
            choice=int(input("Enter Your Purpose choice(1-19):"))
            if(choice ==1):
               customerid=''
               if self.use.calculateTotalOrders(): #1.GetCustomerById
                   print("Totalorders are displayed successfully")
               else:
                   print("Error occured")
            elif(choice ==2):
               customerid=''
               if self.use.GetCustomerDetails():     #GetCustomerByUsername
                   print("Customer details are displayed successfully")
               else:
                   print("Error occured")
            elif(choice ==3):
                customerid = ''
                firstname = ''
                lastname = ''
                email = ''
                phone = ''
                address = ''

                if self.use.UpdateCustomerInfo():       #RegisterCustomer
                   print("Registered successfully")
                else:
                    print("Error Occured")
            elif(choice ==4):
                productid=''
                if self.use.GetProductDetails():
                    print("product details displayed Successfully")
                else:
                    print("Error Occured")
            elif(choice ==5):
                productid = ''
                productname = ''
                pdescription = ''
                price = ''
                if self.use.UpdateProductInfo():
                    print("Updated productinfo successfully")
                else:
                    print("Error occured")
            elif(choice ==6):
                productid=''
                if self.use.IsProductStock():
                    print("productstock is displayed successfully")
                else:
                    print("Error Occured")
            elif(choice ==7):
                orderid=''
                if self.use.CalculateTotalAmount():
                    print("Totalamount is Displayed")
                else:
                    print("Error Occured")
            elif(choice == 8):
                orderid=''

                if self.use.GetOrderDetails():
                    print("Order details are displayed")
                else:
                    print("Error Occured")
            elif(choice ==9):
                orderid = ''
                customerid = ''
                orderdate = ''
                totalamount = ''

                if self.use.UpdateOrderStatus():
                    print("Updated successfully")
                else:
                    print("Error Occured")
            elif(choice ==10):
                orderid =''
                if self.use.CancelOrder():
                    print("order was cancelled")
                else:
                    print("Error Occured")
            elif(choice ==11):
                orderid=''
                if self.use.CalculateSubTotal():
                    print("SubTotal is successfully displayed")
                else:
                    print("Error Ocured")
            elif(choice ==12):
                orderid=''
                if self.use.GetOrderDetailInfo():
                    print("orderdate is Successfully displayed")
                else:
                    print("Error Occured")
            elif(choice ==13):
                orderdetailid = ''
                orderid = ''
                productid = ''
                quantity = ''

                if self.use.UpdateQuantity():
                    print("Quantity is updated successfully")
                else:
                    print("Error Occured")
            elif(choice ==14):
                productid=''

                if self.use.GetProduct():
                    print("Product is displayed")
                else:
                    print("Error Occured")
            elif(choice ==15):
               inventoryid = ''
               if self.use.QuantityInStock():
                    print("Quantityinstock displayed")
               else:
                    print("Error Occured")
            elif(choice ==16):
                inventoryid = ''
                productid = ''
                quantityinstock = ''
                laststockupdate =''
                if self.use.AddToInventory():
                    print("AddToInventory is displayed successfully")
                else:
                    print("Error Occured")
            elif(choice ==17):
                inventoryid=''

                if self.use.RemovefromInventory():
                    print("Removed from Inventory successfully")
                else:
                    print("Error Occured")
            elif(choice ==18):
                inventoryid = ''
                productid = ''
                quantityinstock =''
                laststockupdate = ''

                if self.use.UpdateStockQuantity():
                    print("StockQuantity updated successfully")
                else:
                    print("Error Occured")
            elif(choice ==19):
                inventoryid=''
                if self.use.IsProductAvailable():
                    print("Product Availability displayed successfully")
                else:
                    print("Error Occured")

            else:
                print("Invalid choice.Please Try Later")

obj1=main()
obj1.run()


