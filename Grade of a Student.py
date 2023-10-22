eng=int(input("Enter marks of English: "))
hindi=int(input("Enter marks of Hindi: "))
math=int(input("Enter marks of Math: "))
sci=int(input("Enter marks of Science: "))
sanskrit=int(input("Enter marks of588 Sanskrit: "))
avg=(eng+hindi+math+sci+sanskrit)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")