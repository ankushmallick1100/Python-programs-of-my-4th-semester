import math 
while True:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    d=a+b
    e=a-b
    f=a*b
    g=a/b
    h = int(math.sqrt(a))
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Squre Root")
    print("Enter your choice: ")
    choice=int(input())
    if (choice==1):
        print("Addition is",d)
    elif (choice==2):
        print("Subtraction is: ",e)
    elif (choice==3):
        print("Multiplication is: ",f)
    elif (choice==4):
        print("Division is: ",g)
    elif (choice==5):
        print("Square root of first number is: ",h)
    else:
        print("Invalid input!!  :(")
    ans=input("Do you want to enter again?")
    ans=ans.upper()
    if(ans!='Y'):
       break

