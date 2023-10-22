n = int(input("Enter a number:\n"))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("Perfect number")
else:
    print("Not a Perfect number")