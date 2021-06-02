class cal5:
     def __init__(self):
        
         length = float(input("enter the length of rectangle :"))
         width = float(input("enter the width of rectangle :"))
         self.len= length
         self.wid = width

     def calarea(self):
        area = (self.len * self.wid)
        self.area = area
    
     def display(self):
        print("the area of rectangle is :" , self.area)

cls=cal5()
cls.calarea()
cls.display()