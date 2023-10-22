n = 5
#upper triangle
for i in range(n):
  for j in range(n-i):
    print(' ', end=' ')
  for k in range(2*i+1):
    print('*',end=' ')
  print()
#mid triangle
for i in range(n):
  for j in range(n-i):
    print(' ', end=' ')
  for k in range(2*i+1):
    print('*',end=' ')
  print()
#pole shape
for i in range(n):
  for j in range(n-1):
    print(' ', end=' ')
  print('* * *')