a = int(input('Enter a number:'))
fact = 1
if(a<0) :
    print("Factorial doesn't exist for negative number" )
elif a==0 :
    print('The factorial of 0 is 1')
else :
    for i in range(1,a+1) :
        fact=fact*i
    print('The factorial of this number is ',fact)