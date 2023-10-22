rows=3
for i in range(0,rows):
    for j in range(0,rows):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()