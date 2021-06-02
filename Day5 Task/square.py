class cal4:

    def setdata(self):
        self.number = float(input("enter the number :"))

    def display(self):
        square =( self.number * self.number)
        return square
        
    

cls=cal4()
cls.setdata()
cls.display()
print("square :", cls.display())
