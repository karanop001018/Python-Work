a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
lcm = a
while lcm % b != 0:
  lcm += a
print(f"LCM of {a} and {b} is {lcm}.")