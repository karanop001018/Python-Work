num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
num3 = int(input("Enter third number:\n"))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print(largest)