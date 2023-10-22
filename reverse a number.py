n= 123456
reversed=0
while(n>0):
    dig=n%10
    reversed=reversed*10+dig
    n=n//10
print("Reversed number is:",reversed)