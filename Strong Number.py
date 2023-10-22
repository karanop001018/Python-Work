sum=0
num=145
temp=num
while(num):
    i=1
    fact=1
    r=num%10
    while(i<=r):
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if(sum==temp):
    print("Strong number")
else:
    print("Not a Strong number")