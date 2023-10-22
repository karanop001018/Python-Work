def countVowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in str:
        if i in vowels:
            count += 1
    return count
a = input("Enter a string\n")
print('number of vowels in hello is '+str(countVowels(a)))