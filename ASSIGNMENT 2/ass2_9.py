a = int(input("Enter the range: "))
while a>0 :
    for i in range(1,a+1):
        a = 65
        for j in range(1, i+1):
            print("%c  " %(a), end="")
            a += 1
        print("\n")
    break
