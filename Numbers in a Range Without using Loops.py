def printno(upper):
    if(upper>0):
        printno(upper-1)
        print(upper)
a= int(input("Enter a number:\n"))
printno(a)