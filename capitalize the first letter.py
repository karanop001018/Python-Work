s = input("Enter a string:\n")
newStr = ''
for i in range(len(s)):
  if i == 0 or s[i - 1] == ' ':
    newStr += s[i].upper()
  else:
    newStr += s[i]
print(newStr)