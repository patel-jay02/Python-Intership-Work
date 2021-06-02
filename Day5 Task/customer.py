class scheme:

    def setdatascheme(self):
        self.scheme_id = int(input("enter your scheme_id :"))
        self.scheme_name = input("enter scheme_name :")
        self.outgoing_rate= float(input("enter outgoing_rate :"))
        self.message_charge = float(input("enet message_charge :"))

    def showdatascheme(self):
        print ("scheme detais :")
        print("scheme_id is : ",self.scheme_id)
        print(" schme_name :", self.scheme_name)
        print("outgoing_rate :", self.outgoing_rate)
        print("message_charge :" , self.message_charge)

class customer(scheme):

     def setdatacustomer(self):
         self.cust_id= int(input("enter cust_id :"))
         self.cust_name= input("enter customer name :")
         self.mobile_no = int(input("enter customer mobile no :"))

     def showdatacustomer(self):
        print("customer detais :")
        print("cust_id is :" , self.cust_id)
        print("cust_name is :" , self.cust_name)
        print("mobile_no : ", self.mobile_no)

cls = customer()
cls.setdatascheme()
cls.setdatacustomer()
cls.showdatascheme()
cls.showdatacustomer()