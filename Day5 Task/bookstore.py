class publisher:

    def titlee(self):
        
    
        self.title = "7 habits of highly effective people"
        print(" book title is ", self.title)

class book(publisher):

    def memberdata(self):
        print("page no. of books are 786")

class tape(publisher):

    def time(self):
    
        print("the time of laying tap is 5hrs")
    
b = book()
b.titlee()
b.memberdata()
t=tape()
t.time()
