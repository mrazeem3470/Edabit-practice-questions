for i in range(1,5):
    for space in range(5 - i):
        print(" ",end = "")
    for j in range(i):
        print("*",end=" ")
    print()
for k in range(4,0,-1):
    for space in range(5-k):
        print(" ",end="")
    for j in range(k):
        print("*",end=" ")
    print()
