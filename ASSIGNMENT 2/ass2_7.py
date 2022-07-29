a=int(input("Enter any number: "))
while a>0 :
    for i in range (0,a+1):
        for j in range(0,i):
            print("*",end=" ")
            j=j+1
        print("\n")
    i=i+1
    break