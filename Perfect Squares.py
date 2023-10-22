start = int(input("Enter the Lower bound"))
end = int(input("Enter the upper bound"))
 
for n in range(start, end+1):
    sum = 0

    for i in range(1, n):
      if n%i == 0:
        sum += i
    if n == sum:
      print(n)