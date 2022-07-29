def Tribonacci(x):
    i=3
    a=0
    b=1
    c=1
    print("Tribonacci Series is: \n",end="")
    print(a)
    print(b)
    print(c)
    for i in range(3,x,1):
        sum = a+b+c
        a=b
        b=c
        c=sum
        print(sum)
        print(end="")
        i=i+1
x = int(input("Enter the range:"))
Tribonacci(x)