def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
a=int(input("Enter a number"))
print(factorial(a))