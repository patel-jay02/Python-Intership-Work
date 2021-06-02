class employee:

    def detail(self):
        name = input("enter your name :")
        self.name =name
        designation = input(" enter your designation :")
        self.designation = designation
        

class money(employee):
     def salary(self):
         sal= int(input(" enter your salary :"))
         self.sal = sal
         print(self.name, "," ,self.designation,"," ,self.sal)
        
mo = money()
mo.detail()
mo.salary()
