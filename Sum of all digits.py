n= int(input("Enter a number:\n"))
total=0
while(n>0):
    lastDigit=n%10
    total=total+lastDigit
    n=n//10
print("Total sum of digits in number:",total)