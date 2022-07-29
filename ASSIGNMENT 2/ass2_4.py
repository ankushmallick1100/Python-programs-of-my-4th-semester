a = int(input("Enter a number:"))
if (a<0) :
    print("Please enter a positive number")
else :
    sum = 0
    while a>0 :
        sum = sum + a
        a -= 1
    print('Sum is:',sum)