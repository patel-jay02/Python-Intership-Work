class cal1:


    def setdata(self):
        self.n1=int(input("Enter First number: "))
        self.n2=int(input("Enter Second number: "))
        self.n3=int(input("Enter Third number: "))

    def display(self):
        n=self.n1+self.n2+self.n3
        print("Sum of 3 numbers:",n)

cal=cal1()

cal.setdata()
cal.display()
        