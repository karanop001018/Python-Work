def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))
# another and short approach
print(arr[::-1])