def smallest(x, y, z):
    c = 0
     
    while ( x and y and z ):
        x = x-1
        y = y-1
        z = z-1
        c = c + 1
 
    return c

x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
z = float(input("Enter a number: "))
print("Minimum of 3 numbers is",smallest(x, y, z))
