def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)
print(average([1, 2, 3, 4, 5]))