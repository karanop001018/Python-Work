n = int(input("Enter a number:\n"))
num_digits = len(str(n))
sum = 0
for digit in str(n):
  sum += int(digit)**num_digits
print(sum == n)