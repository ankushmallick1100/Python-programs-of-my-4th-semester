a = int(input("Enter the range: "))
while a>0 :
    for i in range (0,a+1):
        for j in range(0,i):
            print(i,end=" ")
            j=j+1
        print("\n")
        i=i+1
    break