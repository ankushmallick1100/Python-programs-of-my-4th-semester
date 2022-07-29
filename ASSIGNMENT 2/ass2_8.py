a=int(input("Enter any number: "))
while a>0 :
    for i in range (0,a+1):
        for j in range(i,a):
            print("*",end=" ")
            j=j+1
        print("\n")
    i=i+1
    break