arr = ['hello', 'world', 'its', 'assignment', 'website']
for i in range(len(arr)):
  for j in range(i + 1, len(arr)):
    if arr[i] > arr[j]:
      arr[i], arr[j] = arr[j], arr[i]
print(arr)