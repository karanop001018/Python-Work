a = int(input("Enter first number:\n"))
b = int(input("Enter second number:\n"))
if a > b:
  smaller = b
else:
  smaller = a
for i in range(1, smaller+1):
  if (a % i == 0) and (b % i == 0):
    hcf = i
print(f"HCF of {a} and {b} is {hcf}")