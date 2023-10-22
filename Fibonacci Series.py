n = int(input("Enter a number:\n"))
a, b = 0, 1
print(a)
print(b)
for i in range(2, n):
  c = a + b
  print(c)
  a, b = b, c
  
