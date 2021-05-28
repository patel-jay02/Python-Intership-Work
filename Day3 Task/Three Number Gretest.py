a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

# conditions to find largest 
if a>b:
    if a>c:
        g=a
    else:
        g=c
else:
    if b>c:
        g=b
    else:
        g=c

# print the largest number 
print("Greater  = ",g)
